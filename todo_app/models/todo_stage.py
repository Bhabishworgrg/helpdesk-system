# -*- coding: utf-8 -*-

from odoo import fields, models
from odoo.exceptions import UserError


class TodoStage(models.Model):
    _name = 'todo_app.todo_stage'
    _description = 'Todo Stage'
    _order = 'id asc'

    sequence = fields.Integer('Sequence', default=1)
    name = fields.Char('Name', required=True)
    is_prepopulated = fields.Boolean('Is Prepopulated', default=False)

    _sql_constraints = [('name_uniq', 'unique (name)', 'Stage name already exists!')]
    
    def unlink(self):
        if self.search_count([('id', 'in', self.ids), ('is_prepopulated', '=', True)]):
            raise UserError('You cannot delete a prepopulated stage.')
        return super().unlink()
