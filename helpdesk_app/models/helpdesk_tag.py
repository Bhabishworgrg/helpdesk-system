# -*- coding: utf-8 -*-

from odoo import fields, models
from odoo.exceptions import UserError


class HelpdeskTag(models.Model):
    _name = 'helpdesk_app.helpdesk_tag'
    _description = 'Helpdesk Tag'
    _order = 'sequence asc'

    sequence = fields.Integer('Sequence', default=1)
    name = fields.Char('Name', required=True)
    color = fields.Integer('Color', required=True)
    is_prepopulated = fields.Boolean('Is Prepopulated', default=False)

    _sql_constraints = [('name_unique', 'unique(name)', 'Tag name already exists.')]
    
    def unlink(self):
        prepopulated = self.filtered(lambda rec: rec.is_prepopulated)
        if prepopulated:
            raise UserError('You cannot delete a prepopulated tag.')
        return super().unlink()
