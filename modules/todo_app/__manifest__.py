# -*- coding: utf-8 -*-

{
    'name': 'Todo App',
    'version': '0.1',
    'depends': [
        'base_setup',
        'mail',
    ],
    'data': [
        'security/ir_rules.xml',
        'security/ir.model.access.csv',
        'data/ir_cron.xml',
        'wizard/todo_task_complete_wizard.xml',
        'wizard/todo_next_stage_wizard.xml',
        'wizard/todo_restore_wizard.xml',
        'wizard/todo_cancel_wizard.xml',
        'views/todo.xml',
        'views/todo_task.xml',
        'views/menus.xml',
        'views/res_config_settings.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'GPL-3',
}
