# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HelpdeskTicketSendWizard(models.TransientModel):
    _name = 'helpdesk_todo.helpdesk_ticket_send_wizard'
    _description = 'Helpdesk Ticket Send Wizard'

    ticket_id = fields.Many2one('helpdesk_app.helpdesk_ticket', string='Helpdesk Ticket', required=True)
    remark = fields.Text('Remarks', required=True)
    remark_id = fields.Many2one('helpdesk_app.helpdesk_remark', string='Remark')
    todo_id = fields.Many2one('todo_app.todo', string='Todo')
    ticket_title = fields.Char('Title')
    ticket_query =  fields.Text('Query')
    ticket_description = fields.Html('Description')
    ticket_team_member_id = fields.Many2one('res.users', string='Team Member Assigned')
    ticket_leader_id = fields.Many2one('res.users', string='Team Leader')

    def action_confirm(self):
        self.remark_id = self.env['helpdesk_app.helpdesk_remark'].create({
            'ticket_id': self.ticket_id.id,
            'remark': self.remark,
        })

        todo = self.env['todo_app.todo'].create({
            'name': self.ticket_title,
            'user_id': self.ticket_team_member_id.id,
            'leader_id': self.ticket_leader_id.id,
            'summary': self.ticket_query,
            'description': self.ticket_description,
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

    @api.model
    def default_get(self, fields_list):
        defaults = super().default_get(fields_list)
        
        # Get the active ticket from the context
        active_id = self.env.context.get('active_id')
        active_model = self.env.context.get('active_model')
        
        if active_id and active_model:
            ticket = self.env[active_model].browse(active_id)
            defaults.update({
                'ticket_id': ticket.id,
                'ticket_title': ticket.title,
                'ticket_team_member_id': ticket.team_member_id.id,
                'ticket_leader_id': ticket.team_id.leader_id.id,
                'ticket_query': ticket.query,
                'ticket_description': ticket.description,
            })
        return defaults
