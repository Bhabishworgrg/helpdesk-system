# -*- coding: utf-8 -*-

from odoo import fields, models, api


class Todo(models.Model):
    _inherit = 'todo_app.todo'

    stage_id = fields.Many2one('helpdesk_todo.stage', string='Stage', default=lambda self: self.env['helpdesk_todo.stage'].search([('sequence', '=', 1)]), group_expand='_read_group_stage_id')
    ticket_id = fields.Many2one('helpdesk_app.helpdesk_ticket', string='Ticket')
    leader_id = fields.Many2one('res.users', string='Leader')

    def write(self, vals):
        if 'stage_id' in vals:
            self.ticket_id.sudo().write({
                'stage_id': vals['stage_id']
            })
        return super().write(vals)
    
    @api.model
    def _read_group_stage_id(self, records, domain, order=None):
        return records.search([])
