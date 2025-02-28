# -*- coding: utf-8 -*-

from odoo import fields, models, api


class Todo(models.Model):
    _name = 'todo_app.todo'
    _description = 'Todo'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'sequence asc'
   
    sequence = fields.Integer('Sequence', default=1)
    name = fields.Char('Name', required=True, tracking=True)
    active = fields.Boolean('Active', default=True, tracking=True)
    date_deadline = fields.Date('Deadline', default=fields.Date.today, tracking=True)
    summary = fields.Text('Summary', tracking=True)
    description = fields.Html('Description')
    progress = fields.Float('Progress')
    is_complete = fields.Boolean('Is Completed')
    user_id = fields.Many2one('res.users', string='User Assigned', tracking=True)
    task_ids = fields.One2many('todo_app.todo_task', 'todo_id', string='Tasks', tracking=True)
    remark_ids = fields.One2many('todo_app.todo_remark', 'todo_id', string='Remarks')
