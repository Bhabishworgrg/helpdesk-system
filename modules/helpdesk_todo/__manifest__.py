# -*- coding: utf-8 -*-

{
    'name': 'Ticket to Todo',
    'version': '0.1',
    'category': 'Hidden',
    'depends': [
        'helpdesk_app',
        'todo_app',
    ],
    'data': [
        'security/ir_rules.xml',
        'security/ir.model.access.csv',
        'report/ir_actions_report_templates.xml',
        'data/stage_data.xml',
        'wizard/helpdesk_todo_helpdesk_ticket_send_wizard.xml',
        'wizard/helpdesk_todo_helpdesk_ticket_report_wizard.xml',
        'views/stages.xml',
        'views/helpdesk_ticket.xml',
        'views/helpdesk_menus.xml',
        'views/todo.xml',
        'views/todo_menus.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': True,
    'license': 'GPL-3',
}
