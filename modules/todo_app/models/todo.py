# -*- coding: utf-8 -*-

from odoo import fields, models, api


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
    user_id = fields.Many2one('res.users', string='User Assigned', tracking=True)
    task_ids = fields.One2many('todo_app.todo_task', 'todo_id', string='Tasks', tracking=True)
    remark_ids = fields.One2many('todo_app.todo_remark', 'todo_id', string='Remarks')
    
    @api.depends('task_ids', 'task_ids.is_complete')
    def _compute_is_complete(self):
        for rec in self:
            if rec.task_ids:
                rec.is_complete = all(rec.task_ids.mapped('is_complete'))
                rec.progress = len(rec.task_ids.filtered('is_complete')) / len(rec.task_ids) * 100
            else:
                rec.is_complete = False
                rec.progress = 0
