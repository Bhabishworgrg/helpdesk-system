# -*- coding: utf-8 -*-

from odoo import models, fields


class TodoNextStageWizard(models.TransientModel):
    _name = 'helpdesk_todo.todo_next_stage_wizard'
    _description = 'Todo Next Stage Wizard'

    user_id = fields.Many2one('res.users', string='User Responsible')
    todo_id = fields.Many2one('todo_app.todo', string='Todo', required=True)
    remark = fields.Text('Remarks', required=True)

    def action_confirm(self):
        pass
