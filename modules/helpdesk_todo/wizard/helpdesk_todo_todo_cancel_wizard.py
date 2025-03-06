# -*- coding: utf-8 -*-

from odoo import models, fields


class TodoCancelWizard(models.TransientModel):
    _inherit = 'todo_app.todo_cancel_wizard'

    def action_confirm(self):
        self.todo_id.stage_id = self.env.ref('helpdesk_todo.stage_4')
        return super().action_confirm()
