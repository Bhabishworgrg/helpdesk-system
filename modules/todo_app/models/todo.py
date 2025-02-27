# -*- coding: utf-8 -*-

from odoo import fields, models, api


class Todo(models.Model):
    _name = 'todo_app.todo'
    _description = 'Todo'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'sequence asc'
   
    sequence = fields.Integer('Sequence', default=1)
    name = fields.Char('Name', required=True)
    active = fields.Boolean('Active', default=True)
    date_deadline = fields.Date('Deadline', default=fields.Date.today)
    summary = fields.Text('Summary')
    description = fields.Html('Description')
    progress = fields.Float('Progress')
    is_complete = fields.Boolean('Is Completed')
