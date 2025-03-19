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
