# -*- coding: utf-8 -*-

from odoo import models


class Lead(models.Model):
    _inherit = 'crm.lead'

    def action_lead_to_opportunity(self):
        return super().convert_opportunity(None)
