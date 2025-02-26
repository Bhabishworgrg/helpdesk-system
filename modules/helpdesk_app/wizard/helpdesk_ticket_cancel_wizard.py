# -*- coding: utf-8 -*-

from odoo import models, fields


class HelpdeskTicketCancelWizard(models.TransientModel):
    _name = 'helpdesk_app.helpdesk_ticket_cancel_wizard'
    _description = 'Helpdesk Ticket Cancel Wizard'

    user_id = fields.Many2one('res.users', string='User Responsible')
    ticket_id = fields.Many2one('helpdesk_app.helpdesk_ticket', string='Helpdesk Ticket', required=True)
    remarks = fields.Text('Remarks', required=True)
    remark_id = fields.Many2one('helpdesk_app.helpdesk_remark', string='Remark')

    def action_confirm(self):
        self.ticket_id.stage_id = self.env.ref('helpdesk_app.helpdesk_stage_4')
        self.remark_id = self.env['helpdesk_app.helpdesk_remark'].create({
            'ticket_id': self.ticket_id.id,
            'remark': self.remarks,
            'date_time': fields.Datetime.now(),
        })
