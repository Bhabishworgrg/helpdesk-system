# -*- coding: utf-8 -*-

{
    'name': 'Ticket to Lead',
    'version': '0.1',
    'category': 'Hidden',
    'depends': [
        'helpdesk_app',
        'crm',
    ],
    'data': [
        'security/ir.model.access.csv',
        'wizard/helpdesk_crm_crm_lead_create_wizard.xml',
        'views/helpdesk_ticket.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': True,
    'license': 'GPL-3',
}
