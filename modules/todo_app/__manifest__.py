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
        'wizard/todo_task_complete_wizard.xml',
        'wizard/todo_next_stage_wizard.xml',
        'views/todo.xml',
        'views/todo_task.xml',
        'views/menus.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'GPL-3',
}
