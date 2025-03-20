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
    remark_ids = fields.One2many('sale_ext.sale_order_remark', 'sale_order_id', string='Remarks')

    def action_send_for_approval(self):
        for rec in self:
            admin_group = rec.env.ref('sales_team.group_sale_manager')
            rec.message_post(
                body=f'{rec.user_id.name} sent the quotation {rec.name} for approval.',
                partner_ids=admin_group.users.mapped('partner_id').ids,
            )

        self.write({'new_state': 'approval'})

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

    def _confirmation_error_message(self):
        self.ensure_one()
        if self.new_state not in {'draft', 'approved', 'sent'}:
            return _("Some orders are not in a state requiring confirmation.")
        if any(
            not line.display_type
            and not line.is_downpayment
            and not line.product_id
            for line in self.order_line
        ):
            return _("A line on these orders missing a product, you cannot confirm it.")

        return False

    def _prepare_confirmation_values(self):
        values = super()._prepare_confirmation_values()
        values.update({
            'new_state': 'sale'
        })
        return values

    @api.depends('order_line.price_unit', 'order_line.product_template_id.list_price')
    def _compute_need_approval(self):
        for rec in self:
            rec.need_approval = False

            unit_prices = rec.order_line.mapped('price_unit')
            sales_prices = rec.order_line.product_template_id.mapped('list_price')
            for unit_price, sales_price in zip(unit_prices, sales_prices):
                if unit_price < sales_price:
                    rec.need_approval = True
