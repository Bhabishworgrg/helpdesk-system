# -*- coding: utf-8 -*-

from odoo import models, fields


class TodoCancelWizard(models.TransientModel):
    _name = 'todo_app.todo_cancel_wizard'
    _description = 'Todo Cancel Wizard'

    todo_id = fields.Many2one('todo_app.todo', string='Todo', required=True)
    remark = fields.Text('Remarks', required=True)
    remark_id = fields.Many2one('todo_app.todo_remark', string='Remark')

    def action_confirm(self):
        self.remark_id = self.env['todo_app.todo_remark'].create({
            'todo_id': self.todo_id.id,
            'remark': self.remark,
            'date_time': fields.Datetime.now(),
        })
