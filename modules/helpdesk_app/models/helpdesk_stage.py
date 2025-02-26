# *-* coding: utf-8 *-*

from odoo import fields, models
from odoo.exceptions import UserError


class HelpdeskStage(models.Model):
    _name = 'helpdesk_app.helpdesk_stage'
    _description = 'Helpdesk Stage'
    _order = 'sequence asc'

    sequence = fields.Integer('Sequence', default=lambda self: self.search_count([]) + 1)
    name = fields.Char('Name', required=True)
    is_prepopulated = fields.Boolean('Is Prepopulated', default=False)

    def unlink(self):
        if self.search_count([('id', 'in', self.ids), ('is_prepopulated', '=', True)]):
            raise UserError('You cannot delete a prepopulated stage.')
        return super().unlink()
