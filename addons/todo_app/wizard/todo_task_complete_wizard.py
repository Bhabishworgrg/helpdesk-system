# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError


class TodoTaskCompleteWizard(models.TransientModel):
    _name = 'todo_app.todo_task_complete_wizard'
    _description = 'Todo Task Complete Wizard'

    user_id = fields.Many2one('res.users', string='User Responsible')
    task_id = fields.Many2one('todo_app.todo_task', string='Todo Task', required=True)
    remark = fields.Text('Remarks', required=True)

    def action_confirm(self):
        self.ensure_one()
        if not self.task_id:
            raise UserError('Task is not selected')
        self.task_id.action_mark_completed(remark=self.remark)
        return True 
