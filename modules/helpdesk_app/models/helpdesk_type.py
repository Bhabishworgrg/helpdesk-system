# -*- coding: utf-8 -*-

from odoo import fields, models
from odoo.exceptions import UserError


class HelpdeskType(models.Model):
    _name = 'helpdesk_app.helpdesk_type'
    _description = 'Helpdesk Type'
    _order = 'id desc'

    name = fields.Char('Name', required=True)
