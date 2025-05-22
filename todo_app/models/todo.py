# -*- coding: utf-8 -*-

from odoo import fields, models, api, Command
from odoo.exceptions import UserError
from datetime import timedelta


class Todo(models.Model):
    _name = 'todo_app.todo'
    _description = 'Todo'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'sequence asc'
    _rec_name = 'reference_id'
    
    sequence = fields.Integer('Sequence', default=1)
    reference_id = fields.Char(string='Reference ID', required=True, readonly=True, default='New')
    name = fields.Char('Name', required=True, tracking=True)
    active = fields.Boolean('Active', default=True, tracking=True)
    date_deadline = fields.Date('Deadline', default=fields.Date.today, tracking=True)
    summary = fields.Text('Summary', tracking=True)
    description = fields.Html('Description')
    progress = fields.Float('Progress', compute='_compute_is_complete', store=True)
    is_completed_or_cancelled = fields.Boolean('Is Completed or Cancelled', compute='_compute_is_completed_or_cancelled')
    is_complete = fields.Boolean('Is Complete', compute='_compute_is_complete', store=True)
    stage_id = fields.Many2one(
        'todo_app.todo_stage',
        string='Stage',
        default=lambda self: self.env['todo_app.todo_stage'].sudo().search([('sequence', '=', 1)]),    # Set 'Draft'(if not changed) as default stage
        group_expand='_read_group_stage_id',
        tracking=True
    )
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
    partner_id = fields.Many2one(
        'res.partner',
        related='user_id.partner_id',
        string='Partner'
    )

    _sql_constraints = [('name_unique', 'unique(name)', 'Todo name already exists.')]

    @api.model
    def _read_group_stage_id(self, records, domain, order=None):
        return records.search([])
    
    @api.depends('task_ids', 'task_ids.is_complete')
    def _compute_is_complete(self):
        for rec in self:
            if rec.task_ids:
                rec.is_complete = all(rec.task_ids.mapped('is_complete'))
                rec.progress = len(rec.task_ids.filtered('is_complete')) / len(rec.task_ids) * 100
            else:
                rec.is_complete = False
                rec.progress = 0

    @api.depends('stage_id')
    def _compute_is_completed_or_cancelled(self):
        for rec in self:
            rec.is_completed_or_cancelled = rec.stage_id in [
                self.env.ref('todo_app.todo_stage_3'), 
                self.env.ref('todo_app.todo_stage_4'),
            ]
    
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
    
    @api.onchange('todo_template_id')
    def _onchange_todo_template_id(self):
        if self.todo_template_id:
            self.task_ids = [Command.clear()]
            sequence = 1
            tasks_data = []
            for task in self.todo_template_id.task_ids:
                tasks_data.append(
                    Command.create({
                        'sequence': sequence,
                        'name': task.name,
                        'summary': task.summary,
                        'date_deadline': fields.Date.today() + timedelta(days=task.days_deadline),
                    })
                )
                sequence += 1
            self.task_ids = tasks_data
    
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
    
    def action_compose_email(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Send Todo Email',
            'res_model': 'mail.compose.message',
            'view_mode': 'form',
            'views': [(False, 'form')],
            'view_id': False,
            'target': 'new',
            'context': {
                'default_model': 'todo_app.todo',
                'default_res_ids': self.ids,
                'default_composition_mode': 'comment',
                'default_email_layout_xmlid': 'mail.mail_notification_layout_with_responsible_signature',
                'default_template_id': self.env.ref('todo_app.todo_email_template').id,
                'email_notification_allow_footer': True,
                'mark_so_as_sent': True,
            }
        }
    
    def get_portal_url(self):
        return f'/my/todo/{self.id}'

    @api.model_create_multi
    def create(self, vals_list):
        for val in vals_list:
            if val.get('reference_id', ('New')) == 'New':
                val['reference_id'] = self.env['ir.sequence'].next_by_code('todo_app.todo') or 'New'
        return super().create(vals_list)
