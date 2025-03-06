# -*- coding: utf-8 -*-

from odoo import fields, models, api


class HelpdeskTicket(models.Model):
    _name = 'helpdesk_app.helpdesk_ticket'
    _description = 'Helpdesk'
    _rec_name = 'title'
    _order = 'sequence asc'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    sequence = fields.Integer('Sequence', default=1)
    active = fields.Boolean('Active', default=True, tracking=True)
    title = fields.Char('Title', required=True, tracking=True)
    query = fields.Text('Query', required=True, tracking=True)
    description = fields.Html('Description')
    reported_date = fields.Date('Reported Date', default=fields.Date.today)
    category_id = fields.Many2one('helpdesk_app.helpdesk_category', string='Category', default=lambda self: self.env.ref('helpdesk_app.helpdesk_category_1'), tracking=True)
    tag_ids = fields.Many2many('helpdesk_app.helpdesk_tag', string='Tags', tracking=True)
    type_id = fields.Many2one('helpdesk_app.helpdesk_type', string='Type', default=lambda self: self.env.ref('helpdesk_app.helpdesk_type_1'))
    remark_ids = fields.One2many('helpdesk_app.helpdesk_remark', 'ticket_id', string='Remarks')
    team_ids = fields.Many2many('helpdesk_app.helpdesk_team', string='Teams', compute='_compute_team_ids')
    team_id = fields.Many2one('helpdesk_app.helpdesk_team', string='Team', domain="[('id', 'in', team_ids)]", tracking=True)
    team_member_ids = fields.Many2many('res.users', string='Team Members', compute='_compute_team_member_ids')
    team_member_id = fields.Many2one('res.users', string='Team Member', domain='[("id", "in", team_member_ids)]', tracking=True)
    partner_id = fields.Many2one('res.partner', string='Contact', compute='_compute_partner', readonly=False, store=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')

    @api.depends('team_member_id')
    def _compute_team_ids(self):
        for rec in self:
            rec.team_ids = self.env['helpdesk_app.helpdesk_team'].search([('member_ids', 'in', rec.team_member_id.ids)] if rec.team_member_id else [])

    @api.depends('team_id')
    def _compute_team_member_ids(self):
        for rec in self:
            rec.team_member_ids = rec.team_id.member_ids if rec.team_id else self.env['res.users'].search([])

    @api.depends('email', 'phone')
    def _compute_partner(self):
        for rec in self:
            if not rec.env.context.get('from_onchange'):
                rec.partner_id = self.env['res.partner'].search([
                    ('email', '=', rec.email),
                    ('phone', '=', rec.phone)
                ], limit=1)

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        for rec in self:
            if rec.partner_id:
                rec.with_context(from_onchange=True).write({
                    'email': rec.partner_id.email,
                    'phone': rec.partner_id.phone,
                })
            else:
                rec.with_context(from_onchange=True).write({
                    'email': False,
                    'phone': False,
                })
