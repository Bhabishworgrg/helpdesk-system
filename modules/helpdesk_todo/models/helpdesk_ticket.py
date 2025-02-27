# -*- coding: utf-8 -*-

from odoo import fields, models


class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk_app.helpdesk_ticket'

    stage_id = fields.Many2one('helpdesk_todo.stage', string='Stage')
