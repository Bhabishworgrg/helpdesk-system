# -*- coding: utf-8 -*-

from odoo import fields, models


class HelpdeskRemark(models.Model):
    _name = 'helpdesk_app.helpdesk_remark'
    _description = 'Helpdesk Remark'
    _order = 'date_time desc'

    ticket_id = fields.Many2one('helpdesk_app.helpdesk_ticket', string='Ticket', required=True, ondelete='cascade')
    remark = fields.Text('Remark')
    document = fields.Binary('Document')
    date_time = fields.Datetime('Date Time')
