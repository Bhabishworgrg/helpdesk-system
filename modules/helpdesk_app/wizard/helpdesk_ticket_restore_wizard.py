# -*- coding: utf-8 -*-

from odoo import models, fields


class HelpdeskTicketRestoreWizard(models.TransientModel):
    _name = 'helpdesk_app.helpdesk_ticket_restore_wizard'
    _description = 'Helpdesk Ticket Restore Wizard'

    ticket_id = fields.Many2one('helpdesk_app.helpdesk_ticket', string='Helpdesk Ticket', required=True)
    remark = fields.Text('Remarks', required=True)
    remark_id = fields.Many2one('helpdesk_app.helpdesk_remark', string='Remark')

    def action_confirm(self):
        self.remark_id = self.env['helpdesk_app.helpdesk_remark'].create({
            'ticket_id': self.ticket_id.id,
            'remark': self.remark,
        })
