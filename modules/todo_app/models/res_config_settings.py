# -*- coding: utf-8 -*-

from odoo import fields, models, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    todo_notify_days_before = fields.Integer('Notify Days Before Deadline', config_parameter='todo_app.todo_notify_days_before', default=2)
