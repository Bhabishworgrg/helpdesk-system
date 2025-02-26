# -*- coding: utf-8 -*-

from odoo import fields, models, api
from odoo.exceptions import UserError


class HelpdeskTeam(models.Model):
    _name = 'helpdesk_app.helpdesk_team'
    _description = 'Helpdesk Team'

    sequence = fields.Integer('Sequence', default=1)
    name = fields.Char('Name', required=True)
    leader_id = fields.Many2one('res.users', string='Leader', required=True)
    member_ids = fields.Many2many('res.users', string='Members', required=True)

    @api.constrains('leader_id', 'member_ids')
    def _check_leader_is_member(self):
        for team in self:
            if team.leader_id not in team.member_ids:
                raise UserError("The leader must be a member of the team.")

    @api.onchange('member_ids')
    def _onchange_member_ids(self):
        return {
            'domain': { 'leader_id': [('id', 'in', self.member_ids.ids)] }
        }
