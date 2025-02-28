# -*- coding: utf-8 -*-

from odoo import models, fields


class TodoNextStageWizard(models.TransientModel):
    _inherit = 'todo_app.todo_next_stage_wizard'

    def action_confirm(self):
        next_stage = self.env['helpdesk_todo.stage'].search([('sequence', '>', self.todo_id.stage_id.sequence)], limit=1)
        if next_stage:
            self.todo_id.stage_id = next_stage 
        return super().action_confirm()
