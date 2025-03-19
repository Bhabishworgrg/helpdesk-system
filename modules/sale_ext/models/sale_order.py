# -*- coding: utf-8 -*-

from odoo import models, fields, api


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

    @api.depends('order_line.price_unit', 'order_line.product_template_id.list_price')
    def _compute_need_approval(self):
        for rec in self:
            rec.need_approval = False

            unit_prices = rec.order_line.mapped('price_unit')
            sales_prices = rec.order_line.product_template_id.mapped('list_price')
            for unit_price, sales_price in zip(unit_prices, sales_prices):
                if unit_price < sales_price:
                    rec.need_approval = True
