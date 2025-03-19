# -*- coding: utf-8 -*-

from odoo import models, fields


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
