# -*- coding: utf-8 -*-

from odoo import fields, models, api


class HelpdeskTicket(models.Model):
    _name = 'helpdesk_app.helpdesk_ticket'
    _description = 'Helpdesk Ticket'
    _rec_name = 'reference_id'
    _order = 'sequence asc'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    sequence = fields.Integer('Sequence', default=1)
    reference_id = fields.Char(string='Reference ID', required=True, readonly=True, default='New')
    active = fields.Boolean('Active', default=True, tracking=True)
    title = fields.Char('Title', required=True, tracking=True)
    query = fields.Text('Query', tracking=True)
    description = fields.Html('Description')
    reported_date = fields.Date('Reported Date', default=fields.Date.today)

    _sql_constraints = [('title_unique', 'unique(title)', 'Ticket already exists.')]
    
    stage_id = fields.Many2one(
        'helpdesk_app.helpdesk_stage',
        string='Stage',
        default=lambda self: self.env['helpdesk_app.helpdesk_stage'].sudo().search([('sequence', '=', 1)]),    # Set 'Draft'(if not changed) as default stage
        group_expand='_read_group_stage_id',
        tracking=True
    )
    is_completed_or_cancelled = fields.Boolean('Is Completed or Cancelled', compute='_compute_is_completed_or_cancelled')
    is_complete = fields.Boolean('Is Complete', compute='_compute_is_complete', store=True)
    
    category_id = fields.Many2one(
        'helpdesk_app.helpdesk_category', 
        string='Category', 
        default=lambda self: self.env.ref('helpdesk_app.helpdesk_category_1'),  # Set 'General Inquiry'(if not changed) as default category
        tracking=True
    )
    tag_ids = fields.Many2many(
        'helpdesk_app.helpdesk_tag',
        string='Tags',
        tracking=True
    )
    type_id = fields.Many2one(
        'helpdesk_app.helpdesk_type',
        string='Type',
        default=lambda self: self.env.ref('helpdesk_app.helpdesk_type_1'),      # Set 'Internal'(if not changed) as default type
    )
    remark_ids = fields.One2many(
        'helpdesk_app.helpdesk_remark',
        'ticket_id',
        string='Remarks'
    )
    
    partner_id = fields.Many2one(
        'res.partner',
        string='Reporter',
        tracking=True
    )
    partner_email = fields.Char(string='Reporter Email')
    partner_phone = fields.Char(string='Reporter Phone')
    
    team_id = fields.Many2one(
        'helpdesk_app.helpdesk_team',
        string='Team',
        tracking=True
    )
    team_member_ids = fields.Many2many(
        'res.users',
        string='Team Members',
        compute='_compute_team_member_ids',
    )
    team_member_id = fields.Many2one(
        'res.users', 
        string='Team Member',
        domain='[("id", "in", team_member_ids)]',
        tracking=True
    )
    
    @api.depends('stage_id')
    def _compute_is_completed_or_cancelled(self):
        for rec in self:
            rec.is_completed_or_cancelled = rec.stage_id in [
                self.env.ref('helpdesk_app.helpdesk_stage_3'), 
                self.env.ref('helpdesk_app.helpdesk_stage_4'),
            ]

    @api.depends('stage_id')
    def _compute_is_complete(self):
        for rec in self:
            rec.is_complete = rec.stage_id == self.env.ref('helpdesk_app.helpdesk_stage_3')
    
    @api.model
    def _read_group_stage_id(self, records, domain, order=None):
        return records.search([])
    
    @api.depends('team_id')
    def _compute_team_member_ids(self):
        for rec in self:
            if rec.team_id:
                rec.team_member_ids = rec.team_id.member_ids
                if rec.team_member_id and rec.team_member_id.id not in rec.team_id.member_ids.ids:
                    rec.team_member_id = False 
            else:
                rec.team_member_ids = self.env['res.users'].search([])
                rec.team_member_id = False
    
    @api.onchange('team_member_id')
    def _onchange_team_id(self):
        for rec in self:
            if rec.team_member_id and not rec.team_id:
                    rec.team_id = self.env['helpdesk_app.helpdesk_team'].search([('member_ids', 'in', rec.team_member_id.id)], limit=1)

    @api.onchange('partner_email', 'partner_phone')
    def _onchange_partner_email_or_phone(self):
        for rec in self:
            partner = self.env['res.partner'].search(
                [
                    ('email', '=', rec.partner_email),
                    ('phone', '=', rec.partner_phone)
                ],
                limit=1
            )
            if partner:
                rec.partner_id = partner

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        for rec in self:
            if rec.partner_id:
                rec.partner_email = rec.partner_id.email
                rec.partner_phone = rec.partner_id.phone
            else:
                rec.partner_email = False
                rec.partner_phone = False

    @api.model_create_multi
    def create(self, vals_list):
        for val in vals_list:
            if val.get('reference_id', ('New')) == 'New':
                val['reference_id'] = self.env['ir.sequence'].sudo().next_by_code('helpdesk_app.helpdesk_ticket') or 'New'
        rec = super().create(vals_list)
        
        if rec.type_id == rec.env.ref('helpdesk_app.helpdesk_type_2'):
            rec.sudo().message_post(
                body=f'I have a query: {rec.query}',
                partner_ids=rec.env.ref('helpdesk_app.group_helpdesk_manager').sudo().users.mapped('partner_id').ids,
                subtype_xmlid='mail.mt_note',
                email_from=rec.partner_email
            )
        return rec
