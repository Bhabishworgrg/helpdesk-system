# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError


class HelpdeskTicketSendWizard(models.TransientModel):
    _name = 'helpdesk_app.helpdesk_ticket_send_wizard'
    _description = 'Helpdesk Ticket Send Wizard'

    user_id = fields.Many2one('res.users', string='User Responsible')
    ticket_id = fields.Many2one('helpdesk_app.helpdesk_ticket', string='Helpdesk Ticket', required=True)
    remarks = fields.Text('Remarks', required=True)

    def action_confirm(self):
        pass
