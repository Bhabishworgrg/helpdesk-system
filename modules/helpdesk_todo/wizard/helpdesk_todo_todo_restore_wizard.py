# -*- coding: utf-8 -*-

from odoo import models, fields


class TodoRestoreWizard(models.TransientModel):
    _inherit = 'todo_app.todo_restore_wizard'

    def action_confirm(self):        
        self.todo_id.stage_id = self.env['helpdesk_todo.stage'].search([('sequence', '=', 1)])
        return super().action_confirm()
