# -*- coding: utf-8 -*-

from odoo import fields, models
from odoo.exceptions import UserError


class TodoCategory(models.Model):
    _name = 'todo_app.todo_category'
    _description = 'Todo Category'

    name = fields.Char('Name', required=True)
    description = fields.Text('Description')
    is_prepopulated = fields.Boolean('Is Prepopulated', default=False)

    _sql_constraints = [('name_unique', 'unique(name)', 'Category name already exists.')]
    
    def unlink(self):
        prepopulated = self.filtered(lambda rec: rec.is_prepopulated)
        if prepopulated:
            raise UserError('You cannot delete a prepopulated tag.')
        return super().unlink()
