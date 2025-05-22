# -*- coding: utf-8 -*-

from odoo import models, fields


class TodoRestoreWizard(models.TransientModel):
    _name = 'todo_app.todo_restore_wizard'
    _description = 'Todo Restore Wizard'

    todo_id = fields.Many2one('todo_app.todo', string='Todo', required=True)
    remark = fields.Text('Remarks', required=True)
    document = fields.Binary('Document')
    remark_id = fields.Many2one('todo_app.todo_remark', string='Remark')

    def action_confirm(self):
        self.todo_id.stage_id = self.env['todo_app.todo_stage'].search([('sequence', '=', 1)])
        self.remark_id = self.env['todo_app.todo_remark'].create({
            'todo_id': self.todo_id.id,
            'remark': self.remark,
            'document': self.document,
        })
