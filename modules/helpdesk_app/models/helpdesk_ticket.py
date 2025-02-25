# -*- coding: utf-8 -*-

from odoo import fields, models, api, Command, _
from odoo.exceptions import UserError
from datetime import timedelta


class HelpdeskTicket(models.Model):
    _name = 'helpdesk_app.helpdesk_ticket'
    _description = 'Helpdesk'
    _order = 'sequence asc'
    _rec_name = 'title'

    sequence = fields.Integer('Sequence', default=1)
    active = fields.Boolean('Active', default=True)
    title = fields.Char('Title', required=True)
    query = fields.Text('Query', required=True)
    description = fields.Html('Description')
    reported_date = fields.Date('Reported Date', default=fields.Date.today)
    user_id = fields.Many2one('res.users', 'Reported By', default=lambda self: self.env.user)
