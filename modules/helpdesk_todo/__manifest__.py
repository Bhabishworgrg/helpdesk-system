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
        'views/stages.xml',
        'views/helpdesk_menus.xml',
        'views/todo_menus.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'GPL-3',
}
