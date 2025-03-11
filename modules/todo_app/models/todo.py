# -*- coding: utf-8 -*-

from odoo import fields, models, api
from odoo.exceptions import UserError
from datetime import timedelta


class Todo(models.Model):
    _name = 'todo_app.todo'
    _description = 'Todo'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'sequence asc'
   
    sequence = fields.Integer('Sequence', default=1)
    name = fields.Char('Name', required=True, tracking=True)
    active = fields.Boolean('Active', default=True, tracking=True)
    date_deadline = fields.Date('Deadline', default=fields.Date.today, tracking=True)
    summary = fields.Text('Summary', tracking=True)
    description = fields.Html('Description')
    progress = fields.Float('Progress', compute='_compute_is_complete', store=True)
    is_complete = fields.Boolean('Is Completed', compute='_compute_is_complete', store=True)
    user_id = fields.Many2one(
        'res.users',
        string='User Assigned',
        tracking=True
    )
    task_ids = fields.One2many(
        'todo_app.todo_task',
        'todo_id',
        string='Tasks',
        tracking=True
    )
    remark_ids = fields.One2many(
        'todo_app.todo_remark',
        'todo_id',
        string='Remarks'
    )
    category_id = fields.Many2one(
        'todo_app.todo_category',
        string='Category',
        ondelete='set null',
        tracking=True
    )
    todo_template_id = fields.Many2one(
        'todo_app.todo_template',
        string='Todo Template',
        tracking=True
    )

    
    _sql_constraints = [('name_unique', 'unique(name)', 'Todo name already exists.')]

    @api.depends('task_ids', 'task_ids.is_complete')
    def _compute_is_complete(self):
        for rec in self:
            if rec.task_ids:
                rec.is_complete = all(rec.task_ids.mapped('is_complete'))
                rec.progress = len(rec.task_ids.filtered('is_complete')) / len(rec.task_ids) * 100
            else:
                rec.is_complete = False
                rec.progress = 0

    @api.onchange('date_deadline')
    def _onchange_date_deadline(self):
        today = fields.Date.today()
        if self.date_deadline and self.date_deadline < today:
            self.date_deadline = today
            return {
                'warning': {
                    'title': 'Warning',
                    'message': 'Deadline cannot be set to a date in the past',
                }
            }
    
    @api.model
    def _notify_date_deadline(self):
        date_today = fields.Date.today()
        notify_days_before = int(self.env['ir.config_parameter'].sudo().get_param('todo_app.todo_notify_days_before'))
        date_after_days = date_today + timedelta(days=notify_days_before)
        todos = self.search([('date_deadline', '<=', date_after_days), ('date_deadline', '>=', date_today)])
        for rec in todos:
            rec.message_post(
                body=f'Todo {rec.name} is about to expire.',
                partner_ids=rec.user_id.partner_id.ids
            )
