# -*- coding: utf-8 -*-

from odoo import fields, models, api


class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk_app.helpdesk_ticket'

    todo_id = fields.One2many('todo_app.todo', 'ticket_id', string='Todo')
    stage_id = fields.Many2one('helpdesk_todo.stage', string='Stage', default=lambda self: self.env['helpdesk_todo.stage'].search([('sequence', '=', 1)]), group_expand='_read_group_stage_id')
    is_completed_or_cancelled = fields.Boolean(string='Is Completed Stage', compute='_compute_is_completed_or_cancelled')

    @api.depends('stage_id')
    def _compute_is_completed_or_cancelled(self):
        for rec in self:
            rec.is_completed_or_cancelled = rec.stage_id in [
                self.env.ref('helpdesk_todo.stage_3'), 
                self.env.ref('helpdesk_todo.stage_4'),
            ]

    @api.model
    def _read_group_stage_id(self, records, domain, order=None):
        return records.search([])
