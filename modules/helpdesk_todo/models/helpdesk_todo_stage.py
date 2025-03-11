# -*- coding: utf-8 -*-

from odoo import models, fields
from odoo.exceptions import UserError


class HelpdeskTodoStage(models.Model):
    _name = 'helpdesk_todo.stage'
    _description = 'Helpdesk-Todo Stage'
    _order = 'sequence asc'

    sequence = fields.Integer('Sequence', default=lambda self: self.search_count([]) + 1)
    name = fields.Char('Name', required=True)
    is_prepopulated = fields.Boolean('Is Prepopulated', default=False)

    _sql_constraints = [('name_unique', 'unique(name)', 'Stage name already exists.')]

    def unlink(self):
        if self.search_count([('id', 'in', self.ids), ('is_prepopulated', '=', True)]):
            raise UserError('You cannot delete a prepopulated stage.')
        return super().unlink()
