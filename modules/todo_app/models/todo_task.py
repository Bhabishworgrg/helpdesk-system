# -*- coding: utf-8 -*-

from odoo import fields, models, api


class TodoTask(models.Model):
    _name = 'todo_app.todo_task'
    _description = 'Todo Task'
    _order = 'sequence asc'

    sequence = fields.Integer('Sequence')
    name = fields.Char('Name', required=True)
    date_deadline = fields.Date('Date Deadline')
    is_complete = fields.Boolean('Is Completed', default=False)
    user_id = fields.Many2one('res.users', string='User Assigned')
