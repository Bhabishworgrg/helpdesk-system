# -*- coding: utf-8 -*-

{
    'name': 'Helpdesk App',
    'icon': '/helpdesk_app/static/description/helpdesk.png',
    'author': 'Bhabishwor Gurung',
    'depends': [
        'base_setup',
        'mail',
        'website',
    ],
    'data': [
        'security/ir_rules.xml',
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'data/helpdesk_category_data.xml',
        'data/helpdesk_tag_data.xml',
        'data/helpdesk_type_data.xml',
        'wizard/helpdesk_ticket_cancel_wizard.xml',
        'wizard/helpdesk_ticket_restore_wizard.xml',
        'views/portal_templates.xml',
        'views/website_templates.xml',
        'views/helpdesk_ticket.xml',
        'views/helpdesk_category.xml',
        'views/helpdesk_tag.xml',
        'views/helpdesk_type.xml',
        'views/helpdesk_team.xml',
        'views/menus.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'GPL-3',
}
