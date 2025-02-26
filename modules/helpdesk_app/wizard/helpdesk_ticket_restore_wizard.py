# -*- coding: utf-8 -*-

from odoo import models, fields


class HelpdeskTicketRestoreWizard(models.TransientModel):
    _name = 'helpdesk_app.helpdesk_ticket_restore_wizard'
    _description = 'Helpdesk Ticket Restore Wizard'

    user_id = fields.Many2one('res.users', string='User Responsible')
    ticket_id = fields.Many2one('helpdesk_app.helpdesk_ticket', string='Helpdesk Ticket', required=True)
    remarks = fields.Text('Remarks', required=True)

    def action_confirm(self):
        self.ticket_id.stage_id = self.env['helpdesk_app.helpdesk_stage'].search([('sequence', '=', 1)])
