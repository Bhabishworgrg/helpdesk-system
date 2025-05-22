# -*- coding: utf-8 -*-

from odoo import fields, models, api


class Todo(models.Model):
    _inherit = 'todo_app.todo'

    merged_stage_id = fields.Many2one('helpdesk_todo.stage', string='Stage', default=lambda self: self.env['helpdesk_todo.stage'].search([('sequence', '=', 1)]), group_expand='_read_group_merged_stage_id')
    ticket_id = fields.Many2one('helpdesk_app.helpdesk_ticket', string='Ticket')
    leader_id = fields.Many2one('res.users', string='Leader')
    is_completed_or_cancelled = fields.Boolean(string='Is Completed Stage', compute='_compute_is_completed_or_cancelled')

    @api.depends('merged_stage_id')
    def _compute_is_completed_or_cancelled(self):
        for rec in self:
            rec.is_completed_or_cancelled = rec.merged_stage_id in [
                self.env.ref('helpdesk_todo.stage_3'), 
                self.env.ref('helpdesk_todo.stage_4'),
            ]

    def write(self, vals):
        if 'merged_stage_id' in vals:
            self.ticket_id.sudo().write({
                'merged_stage_id': vals['merged_stage_id']
            })
        return super().write(vals)
    
    @api.model
    def _read_group_merged_stage_id(self, records, domain, order=None):
        return records.search([])

    @api.model
    def create(self, vals):
        rec = super().create(vals)
        if rec.ticket_id:
            rec.message_post(
                body=f'Todo {rec.name} has been assigned to {rec.user_id.partner_id.name}',
                partner_ids=rec.leader_id.partner_id.ids,
                subtype_xmlid="mail.mt_note"
            )
        return rec
