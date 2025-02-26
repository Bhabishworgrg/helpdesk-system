# -*- coding: utf-8 -*-

{
    'name': 'Helpdesk System',
    'version': '0.1',
    'depends': [
        'base_setup',
        'mail',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/helpdesk_category_data.xml',
        'data/helpdesk_tag_data.xml',
        'data/helpdesk_stage_data.xml',
        'data/helpdesk_type_data.xml',
        'wizard/helpdesk_ticket_send_wizard.xml',
        'views/helpdesk_ticket.xml',
        'views/helpdesk_category.xml',
        'views/helpdesk_tag.xml',
        'views/helpdesk_stage.xml',
        'views/helpdesk_type.xml',
        'views/menus.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'GPL-3',
}
