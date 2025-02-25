# -*- coding: utf-8 -*-

from odoo import fields, models
from odoo.exceptions import UserError

class HelpdeskCategory(models.Model):
    _name = 'helpdesk_app.helpdesk_category'
    _description = 'Helpdesk Category'
    _order = 'sequence asc'

    sequence = fields.Integer('Sequence', default=1)
    name = fields.Char('Name', required=True)
    description = fields.Text('Description')
    is_prepopulated = fields.Boolean('Is Prepopulated', default=False)

    def unlink(self):
        if self.search_count([('id', 'in', self.ids), ('is_prepopulated', '=', True)]):
            raise UserError('You cannot delete a prepopulated category.')
        return super().unlink()
