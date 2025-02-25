# -*- coding: utf-8 -*-

{
    'name': 'Helpdesk System',
    'version': '0.1',
    'depends': [
        'base_setup'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/helpdesk_ticket.xml',
        'views/helpdesk_category.xml',
        'views/menus.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'GPL-3',
}
