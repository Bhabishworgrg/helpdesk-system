# *-* coding: utf-8 *-*

from odoo import fields, models


class HelpdeskStage(models.Model):
    _name = 'helpdesk_app.helpdesk_stage'
    _description = 'Helpdesk Stage'
    _order = 'sequence asc'

    sequence = fields.Integer('Sequence', default=1)
    name = fields.Char('Name', required=True)
