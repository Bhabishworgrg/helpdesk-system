# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Lead(models.Model):
    _inherit = 'crm.lead'

    is_lost = fields.Boolean(string='Is Lost', default=False, compute='_compute_is_lost')
    prev_stage_id = fields.Many2one('crm.stage', string='Previous Stage')

    @api.depends('stage_id')
    def _compute_is_lost(self):
        for rec in self:
            lost_stage = self.env.ref('crm_ext.stage_lead5')
            rec.is_lost = rec.stage_id == lost_stage 
    
    def action_lead_to_opportunity(self):
        return super().convert_opportunity(None)

    def action_restore(self):
        self.write({
            'lost_reason_id': False,
            'stage_id': self.prev_stage_id.id
        })
        self._compute_probabilities()

    def write(self, values):
        if 'stage_id' in values:
            self.prev_stage_id = self.stage_id
        return super().write(values)
