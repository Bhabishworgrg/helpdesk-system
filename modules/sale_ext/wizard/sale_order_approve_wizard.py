# -*- coding: utf-8 -*-

from odoo import models, fields


class SaleOrderApproveWizard(models.TransientModel):
    _name = 'sale_ext.sale_order_approve_wizard'
    _description = 'Sale Order Approve Wizard'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    sale_order_id = fields.Many2one('sale.order', string='Sale Order', required=True)
    remark = fields.Text('Remarks', required=True)
    document = fields.Binary('Document')
    remark_id = fields.Many2one('sale_ext.sale_order_remark', string='Remark')

    def action_confirm(self):
        sale_order = self.sale_order_id
        sale_order.message_post(
            body=f'Quotation {sale_order.name} was approveed.',
            partner_ids=sale_order.user_id.partner_id.ids
        )

        sale_order.write({'new_state': 'approved'})
        
        self.remark_id = self.env['sale_ext.sale_order_remark'].create({
            'sale_order_id': sale_order.id,
            'remark': self.remark,
            'document': self.document,
        })
