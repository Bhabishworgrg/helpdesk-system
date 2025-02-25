# -*- coding: utf-8 -*-

from odoo import fields, models


class HelpdeskCategory(models.Model):
    _name = 'helpdesk_app.helpdesk_category'
    _description = 'Helpdesk Category'
    _order = 'sequence asc'

    sequence = fields.Integer('Sequence', default=1)
    name = fields.Char('Name', required=True)
    description = fields.Text('Description')
