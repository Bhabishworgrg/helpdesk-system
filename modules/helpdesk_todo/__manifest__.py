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
        'security/ir.model.access.csv',
        'data/stage_data.xml',
        'wizard/helpdesk_todo_todo_next_stage_wizard.xml',
        'wizard/helpdesk_todo_helpdesk_ticket_send_wizard.xml',
        'views/stages.xml',
        'views/helpdesk_ticket.xml',
        'views/helpdesk_menus.xml',
        'views/todo.xml',
        'views/todo_menus.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'GPL-3',
}
