# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CRMLeadCreateWizard(models.TransientModel):
    _name = 'helpdesk_crm.crm_lead_create_wizard'
    _description = 'CRM Lead Create Wizard'

    ticket_id = fields.Many2one('helpdesk_app.helpdesk_ticket', string='Helpdesk Ticket', required=True)
    remark = fields.Text('Remarks', required=True)
    remark_id = fields.Many2one('helpdesk_app.helpdesk_remark', string='Remark')
    lead_id = fields.Many2one('crm.lead', string='Lead')
    title = fields.Char('Title', required=True)
    partner_id = fields.Many2one('res.partner', string='Contact')

    def action_confirm(self):
        self.remark_id = self.env['helpdesk_app.helpdesk_remark'].create({
            'ticket_id': self.ticket_id.id,
            'remark': self.remark,
            'date_time': fields.Datetime.now(),
        })

        lead = self.env['crm.lead'].create({
            'name': self.title,
            'partner_id': self.partner_id.id,
        })
        self.lead_id = lead.id
        
        return {
            'name': 'Lead',
            'view_mode': 'form',
            'res_model': 'crm.lead',
            'type': 'ir.actions.act_window',
            'res_id': lead.id,
            'target': 'current',
        }

    @api.model
    def default_get(self, fields_list):
        defaults = super().default_get(fields_list)
        
        # Get the active ticket from the context
        active_id = self.env.context.get('active_id')
        active_model = self.env.context.get('active_model')
        
        if active_id and active_model:
            ticket = self.env[active_model].browse(active_id)
            defaults.update({
                'title': ticket.title,
                'partner_id': ticket.partner_id.id,
            })
        return defaults
