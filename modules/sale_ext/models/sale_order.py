# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError


NEW_SALE_ORDER_STATE = [
    ('draft', 'Quotation'),
    ('approval', 'Sent for Approval'),
    ('approved', 'Approved'),
    ('sent', 'Quotation Sent'),
    ('sale', 'Sales Order'),
    ('cancel', 'Cancelled'),
]


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    new_state = fields.Selection(NEW_SALE_ORDER_STATE, string='Status', readonly=True, default='draft')
    need_approval = fields.Boolean('Need Approval', compute='_compute_need_approval', store=True)
        
    def action_send_for_approval(self):
        self.write({'new_state': 'approval'})

    def action_approve(self):
        self.write({'new_state': 'approved'})

    def action_reject(self):
        self.write({'new_state': 'draft'})

    @api.returns('mail.message', lambda value: value.id)
    def message_post(self, **kwargs):
        res = super().message_post(**kwargs)
        if self.env.context.get('mark_so_as_sent'):
            draft_or_approved = self.filtered(lambda o: o.new_state in ['draft', 'approved'])
            draft_or_approved.with_context(tracking_disable=True).write({
                'new_state': 'sent'
            })
        return res 
    
    def action_cancel(self):
        if not self.env.context.get('disable_cancel_warning'):
            inv = self.invoice_ids.filtered(lambda inv: inv.new_state == 'draft')
            inv.button_cancel()
            self.write({'new_state': 'cancel'})
        return super().action_cancel()


    def action_draft(self):
        orders = self.filtered(lambda s: s.new_state in ['cancel', 'sent'])
        orders.write({'new_state': 'draft'})
        return super().action_draft()

    def action_confirm(self):
        self.ensure_one()
        if self.new_state not in {'draft', 'approved', 'sent'}:
            raise UserError(_('Some orders are not in a state requiring confirmation.'))
        if any(
            not line.display_type
            and not line.is_downpayment
            and not line.product_id
            for line in self.order_line
        ):
            raise UserError(_('A line on these orders missing a product, you cannot confirm it.'))

        self.order_line._validate_analytic_distribution()

        for order in self:
            if order.partner_id in order.message_partner_ids:
                continue
            order.message_subscribe([order.partner_id.id])

        self.write({
            'new_state': 'sale',
            'date_order': fields.Datetime.now()
        })

        context = self._context.copy()
        context.pop('default_name', None)

        self.with_context(context)._action_confirm()
        user = self[:1].create_uid
        if user and user.sudo().has_group('sale.group_auto_done_setting'):
            self.action_lock()

        if self.env.context.get('send_email'):
            self._send_order_confirmation_mail()

        return True

    @api.depends('order_line.price_unit', 'order_line.product_template_id.list_price')
    def _compute_need_approval(self):
        for rec in self:
            rec.need_approval = False

            unit_prices = rec.order_line.mapped('price_unit')
            sales_prices = rec.order_line.product_template_id.mapped('list_price')
            for unit_price, sales_price in zip(unit_prices, sales_prices):
                if unit_price < sales_price:
                    rec.need_approval = True
