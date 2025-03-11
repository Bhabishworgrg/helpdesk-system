# -*- coding: utf-8 -*-

from odoo import fields, models
from odoo.exceptions import UserError


class TodoTemplate(models.Model):
    _name = 'todo_app.todo_template'
    _description = 'Todo Template'
    _order = 'id desc'

    def unlink(self):
        prepopulated = self.filtered(lambda rec: rec.is_prepopulated)
        if prepopulated:
            raise UserError('You cannot delete a prepopulated template.')
        return super().unlink()
    
    name = fields.Char('Name', required=True)
    description = fields.Text('Description')
    task_ids = fields.One2many('todo_app.template_tasks', 'task_template_id')
    
    _sql_constraints = [('name_uniq', 'unique (name)', 'Template name already exists!')]


class TemplateTasks(models.Model):
    _name = 'todo_app.template_tasks'
    _description = 'Template Tasks'
    _order = 'id desc'

    task_template_id = fields.Many2one('todo_app.task_template', string='Todo Template', required=True)
    sequence = fields.Integer('Sequence', default=1)
    name = fields.Char('Name', required=True)
    summary = fields.Text('Summary')
    days_deadline = fields.Integer('Due in', default=5)
    
    _sql_constraints = [('name_uniq', 'unique (name, task_template_id)', 'Task name already exists!')]
