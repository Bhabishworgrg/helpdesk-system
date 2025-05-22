# -*- coding: utf-8 -*-

{
    'name': 'Ticket to Lead',
    'summary': 'Convert Helpdesk Tickets to CRM Leads',
    'author': 'Bhabishwor Gurung',
    'category': 'Hidden',
    'depends': [
        'helpdesk_app',
        'crm',
        'helpdesk_todo',
    ],
    'data': [
        'security/ir.model.access.csv',
        'wizard/helpdesk_crm_crm_lead_create_wizard.xml',
        'views/helpdesk_ticket.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': True,
    'license': 'MIT',
}
