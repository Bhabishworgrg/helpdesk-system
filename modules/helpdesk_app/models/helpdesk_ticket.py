# -*- coding: utf-8 -*-

from odoo import fields, models


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
    category_id = fields.Many2one('helpdesk_app.helpdesk_category', string='Category')
    tag_ids = fields.Many2many('helpdesk_app.helpdesk_tag', string='Tags')
    stage_id = fields.Many2one('helpdesk_app.helpdesk_stage', string='Stage', default=lambda self: self.env.ref('helpdesk_app.helpdesk_stage_1'))
    type_id = fields.Many2one('helpdesk_app.helpdesk_type', string='Type')
    is_completed_or_cancelled = fields.Boolean('Is Completed or Cancelled', compute='_compute_is_completed_or_cancelled')

    def _compute_is_completed_or_cancelled(self):
        for rec in self:
            rec.is_completed_or_cancelled = rec.stage_id in [self.env.ref('helpdesk_app.helpdesk_stage_3'), self.env.ref('helpdesk_app.helpdesk_stage_4')]

#    def action_next_stage(self):
#        next_stage = self.env['helpdesk_app.helpdesk_stage'].search([('sequence', '>', self.stage_id.sequence)], limit=1)
#        if next_stage:
#            self.stage_id = next_stage 
#
