# -*- coding: utf-8 -*-

from odoo import fields, models
from odoo.exceptions import UserError


class HelpdeskTag(models.Model):
    _name = 'helpdesk_app.helpdesk_tag'
    _description = 'Helpdesk Tag'
    _order = 'sequence asc'

    sequence = fields.Integer('Sequence', default=1)
    name = fields.Char('Name', required=True)
    color = fields.Integer('Color', required=True)
    is_prepopulated = fields.Boolean('Is Prepopulated', default=False)

    def unlink(self):
        if self.search_count([('id', 'in', self.ids), ('is_prepopulated', '=', True)]):
            raise UserError('You cannot delete a prepopulated tag.')
        return super().unlink()
