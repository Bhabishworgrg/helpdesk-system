# -*- coding: utf-8 -*-

from odoo import fields, models


class SaleOrderRemark(models.Model):
    _name = 'sale_ext.sale_order_remark'
    _description = 'Sale Order Remark'
    _order = 'date_time desc'

    sale_order_id = fields.Many2one('sale.order', string='Sale Order', required=True, ondelete='cascade')
    remark = fields.Text('Remark')
    document = fields.Binary('Document')
    date_time = fields.Datetime('Date Time', default=fields.Datetime.now)
