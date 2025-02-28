# -*- coding: utf-8 -*-

from odoo import fields, models


class TodoRemark(models.Model):
    _name = 'todo_app.todo_remark'
    _description = 'Todo Remark'
    _order = 'date_time desc'

    todo_id = fields.Many2one('todo_app.todo', string='Todo', required=True, ondelete='cascade')
    remark = fields.Text('Remark')
    document = fields.Binary('Document')
    date_time = fields.Datetime('Date Time')
