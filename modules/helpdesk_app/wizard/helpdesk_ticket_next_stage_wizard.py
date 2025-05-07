# -*- coding: utf-8 -*-

from odoo import models, fields


class HelpdeskTicketNextStageWizard(models.TransientModel):
    _name = 'helpdesk_app.helpdesk_ticket_next_stage_wizard'
    _description = 'Helpdesk Ticket Next Stage Wizard'

    user_id = fields.Many2one('res.users', string='User Responsible')
    ticket_id = fields.Many2one('helpdesk_app.helpdesk_ticket', string='Helpdesk Ticket', required=True)
    remark = fields.Text('Remarks', required=True)
    document = fields.Binary('Document')
    remark_id = fields.Many2one('helpdesk_app.helpdesk_remark', string='Remark')

    def action_confirm(self):
        next_stage = self.env['helpdesk_app.helpdesk_stage'].search([('sequence', '>', self.ticket_id.stage_id.sequence)], limit=1)
        if next_stage:
            self.ticket_id.stage_id = next_stage 
        
        self.remark_id = self.env['helpdesk_app.helpdesk_remark'].create({
            'ticket_id': self.ticket_id.id,
            'remark': self.remark,
            'document': self.document,
        })

