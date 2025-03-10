# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError


class HelpdeskTicketReportWizard(models.TransientModel):
    _name = 'helpdesk_todo.helpdesk_ticket_report_wizard'
    _description = 'Helpdesk Ticket Report Wizard'

    from_date = fields.Date('From Date', required=True)
    to_date = fields.Date('To Date', required=True)

    def action_create_report(self):
        self.ensure_one()
        if self.from_date > self.to_date:
            raise UserError('From Date cannot be greater than To Date.')

        tickets = self.env['helpdesk_app.helpdesk_ticket'].search([
            ('reported_date', '>=', self.from_date),
            ('reported_date', '<=', self.to_date),
        ])

        processed_tickets = []
        for ticket in tickets.read([
            'title', 'stage_id', 'reported_date', 'category_id', 'partner_id', 'team_member_id'
        ]):
            for field in ['category_id', 'partner_id', 'team_member_id']:
                if not ticket.get(field):
                    ticket[field] = (False, '')
            processed_tickets.append(ticket)

        stage_counts = {}
        for ticket in tickets:
            stage_name = ticket.stage_id.name
            stage_counts[stage_name] = stage_counts.get(stage_name, 0) + 1

        data = {
            'from_date': self.from_date,
            'to_date': self.to_date,
            'tickets': processed_tickets,
            'stage_counts': stage_counts,
            'total_tickets': len(tickets),
        }

        return self.env.ref('helpdesk_todo.action_helpdesk_report').report_action(self, data)
