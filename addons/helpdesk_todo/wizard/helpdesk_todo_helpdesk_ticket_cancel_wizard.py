# -*- coding: utf-8 -*-

from odoo import models, fields


class HelpdeskTicketCancelWizard(models.TransientModel):
    _inherit = 'helpdesk_app.helpdesk_ticket_cancel_wizard'

    def action_confirm(self):
        self.ticket_id.todo_id.merged_stage_id = self.ticket_id.merged_stage_id = self.env.ref('helpdesk_todo.stage_4')
        return super().action_confirm()
