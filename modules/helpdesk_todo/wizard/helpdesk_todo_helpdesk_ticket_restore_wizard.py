# -*- coding: utf-8 -*-

from odoo import models, fields


class HelpdeskTicketRestoreWizard(models.TransientModel):
    _inherit = 'helpdesk_app.helpdesk_ticket_restore_wizard'

    def action_confirm(self):        
        self.ticket_id.todo_id.stage_id = self.ticket_id.stage_id = self.env['helpdesk_todo.stage'].search([('sequence', '=', 1)])
        return super().action_confirm()
