# -*- coding: utf-8 -*-

from odoo import fields, models, api


class HelpdeskTicket(models.Model):
    _name = 'helpdesk_app.helpdesk_ticket'
    _description = 'Helpdesk'
    _rec_name = 'title'
    _order = 'sequence asc'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    sequence = fields.Integer('Sequence', default=1)
    active = fields.Boolean('Active', default=True)
    title = fields.Char('Title', required=True)
    query = fields.Text('Query', required=True)
    description = fields.Html('Description')
    reported_date = fields.Date('Reported Date', default=fields.Date.today)
    user_id = fields.Many2one('res.users', 'Reported By', default=lambda self: self.env.user)
    category_id = fields.Many2one('helpdesk_app.helpdesk_category', string='Category', default=lambda self: self.env.ref('helpdesk_app.helpdesk_category_1'))
    tag_ids = fields.Many2many('helpdesk_app.helpdesk_tag', string='Tags')
    type_id = fields.Many2one('helpdesk_app.helpdesk_type', string='Type', default=lambda self: self.env.ref('helpdesk_app.helpdesk_type_1'))
    remark_ids = fields.One2many('helpdesk_app.helpdesk_remark', 'ticket_id', string='Remarks')
    team_id = fields.Many2one('helpdesk_app.helpdesk_team', string='Team')
    team_member_ids = fields.Many2many('res.users', string='Team Members', related='team_id.member_ids')
    team_member_id = fields.Many2one('res.users', string='Team Member', domain='[("id", "in", team_member_ids)]')

#    def action_next_stage(self):
#        next_stage = self.env['helpdesk_app.helpdesk_stage'].search([('sequence', '>', self.stage_id.sequence)], limit=1)
#        if next_stage:
#            self.stage_id = next_stage 
#
