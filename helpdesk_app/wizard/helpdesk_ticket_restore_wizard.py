# -*- coding: utf-8 -*-

from odoo import models, fields


class HelpdeskTicketRestoreWizard(models.TransientModel):
    _name = 'helpdesk_app.helpdesk_ticket_restore_wizard'
    _description = 'Helpdesk Ticket Restore Wizard'

    ticket_id = fields.Many2one('helpdesk_app.helpdesk_ticket', string='Helpdesk Ticket', required=True)
    remark = fields.Text('Remarks', required=True)
    document = fields.Binary('Document')
    remark_id = fields.Many2one('helpdesk_app.helpdesk_remark', string='Remark')

    def action_confirm(self):
        self.ticket_id.stage_id = self.env['helpdesk_app.helpdesk_stage'].search([('sequence', '=', 1)])
        self.remark_id = self.env['helpdesk_app.helpdesk_remark'].create({
            'ticket_id': self.ticket_id.id,
            'remark': self.remark,
            'document': self.document,
        })
