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
        'data/todo_category_data.xml',
        'data/todo_template_data.xml',
        'wizard/todo_task_complete_wizard.xml',
        'wizard/todo_next_stage_wizard.xml',
        'wizard/todo_restore_wizard.xml',
        'wizard/todo_cancel_wizard.xml',
        'views/website_templates.xml',
        'views/todo.xml',
        'views/todo_task.xml',
        'views/todo_category.xml',
        'views/todo_template.xml',
        'views/res_config_settings.xml',
        'views/menus.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'GPL-3',
}
