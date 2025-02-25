# -*- coding: utf-8 -*-

from odoo import fields, models


class HelpdeskTag(models.Model):
    _name = 'helpdesk_app.helpdesk_tag'
    _description = 'Helpdesk Tag'
    _order = 'sequence asc'

    sequence = fields.Integer('Sequence', default=1)
    name = fields.Char('Name', required=True)
    color = fields.Integer('Color', required=True)
