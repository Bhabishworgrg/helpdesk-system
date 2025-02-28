# -*- coding: utf-8 -*-

from odoo import models, fields


class HelpdeskTicketSendWizard(models.TransientModel):
    _name = 'helpdesk_todo.helpdesk_ticket_send_wizard'
    _description = 'Helpdesk Ticket Send Wizard'

    user_id = fields.Many2one('res.users', string='User Responsible')
    ticket_id = fields.Many2one('helpdesk_app.helpdesk_ticket', string='Helpdesk Ticket', required=True)
    remark = fields.Text('Remarks', required=True)
    remark_id = fields.Many2one('helpdesk_app.helpdesk_remark', string='Remark')
    todo_id = fields.Many2one('todo_app.todo', string='Todo')

    def action_confirm(self):
        self.remark_id = self.env['helpdesk_app.helpdesk_remark'].create({
            'ticket_id': self.ticket_id.id,
            'remark': self.remark,
            'date_time': fields.Datetime.now(),
        })

        todo = self.env['todo_app.todo'].create({
            'name': self.ticket_id.title,
            'user_id': self.ticket_id.team_member_id.id,
            'summary': self.ticket_id.query,
            'description': self.ticket_id.description,
        })
        self.todo_id = todo.id
        return {
            'name': 'Todo',
            'view_mode': 'form',
            'res_model': 'todo_app.todo',
            'type': 'ir.actions.act_window',
            'res_id': todo.id,
            'target': 'current',
        }
