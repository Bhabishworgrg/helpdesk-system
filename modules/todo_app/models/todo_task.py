# -*- coding: utf-8 -*-

from odoo import fields, models, api


class TodoTask(models.Model):
    _name = 'todo_app.todo_task'
    _description = 'Todo Task'
    _order = 'sequence asc'

    sequence = fields.Integer('Sequence')
    name = fields.Char('Name', required=True)
    summary = fields.Text('Summary')
    date_deadline = fields.Date('Date Deadline')
    is_complete = fields.Boolean('Is Completed', default=False)
    user_id = fields.Many2one('res.users', string='User Assigned')
    todo_id = fields.Many2one('todo_app.todo', string='Todo', required=True, ondelete='cascade')
    remark = fields.Text('Remark')
    
    def action_mark_completed(self, remark):
        self.write({
            'is_complete': True,
            'remark': remark
        })
        return True
