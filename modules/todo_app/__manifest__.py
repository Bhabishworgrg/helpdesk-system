# -*- coding: utf-8 -*-

{
    'name': 'Todo App',
    'version': '0.1',
    'depends': [
        'base_setup',
        'mail',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/todo.xml',
        'views/menus.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'GPL-3',
}
