# -*- coding: utf-8 -*-

from odoo import fields, models, api


class Todo(models.Model):
    _inherit = 'todo_app.todo'

    stage_id = fields.Many2one('helpdesk_todo.stage', string='Stage')
    ticket_id = fields.Many2one('helpdesk_app.helpdesk_ticket', string='Ticket')

    def write(self, vals):
        if 'stage_id' in vals:
            self.ticket_id.write({
                'stage_id': vals['stage_id']
            })
        return super().write(vals)
