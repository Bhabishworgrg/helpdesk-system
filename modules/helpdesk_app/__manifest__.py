# -*- coding: utf-8 -*-

{
    'name': 'Helpdesk System',
    'version': '0.1',
    'depends': [
        'base_setup'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/helpdesk_category_data.xml',
        'views/helpdesk_ticket.xml',
        'views/helpdesk_category.xml',
        'views/helpdesk_tag.xml',
        'views/menus.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'GPL-3',
}
