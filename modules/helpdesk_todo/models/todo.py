# -*- coding: utf-8 -*-

from odoo import fields, models, api


class Todo(models.Model):
    _inherit = 'todo_app.todo'

    stage_id = fields.Many2one('helpdesk_todo.stage', string='Stage')
