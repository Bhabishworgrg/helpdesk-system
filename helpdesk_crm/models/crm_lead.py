# -*- coding: utf-8 -*-

from odoo import fields, models


class Lead(models.Model):
    _inherit = 'crm.lead'

    ticket_id = fields.Many2one('helpdesk_app.helpdesk_ticket', string='Helpdesk Ticket')

    def write(self, vals):
        res = super().write(vals)
        for rec in self:
            if rec.stage_id == self.env.ref('crm.stage_lead4') or rec.active == False:
                rec.ticket_id.write({
                    'merged_stage_id': self.env.ref('helpdesk_todo.stage_3').id,
                })
        return res 
