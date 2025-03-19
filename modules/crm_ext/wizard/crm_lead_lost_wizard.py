# -*- coding: utf-8 -*-

from odoo import models, fields


class CrmLeadLost(models.TransientModel):
    _inherit = 'crm.lead.lost'

    def action_mark_as_lost(self):
        self.ensure_one()
        lost_stage = self.env.ref('crm_ext.stage_lead5')
        res = self.lead_ids.action_set_lost(
            stage_id=lost_stage.id,
            active=True,
            lost_reason_id=self.lost_reason_id.id
        )
        return res
