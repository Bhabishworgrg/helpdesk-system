# -*- coding: utf-8 -*-

{
    'name': 'CRM Extension',
    'author': 'Bhabishwor Gurung',
    'category': 'Hidden',
    'depends': [
        'crm',
    ],
    'data': [
        'data/crm_stage_data.xml',
        'wizard/crm_lead_lost_wizard.xml',
        'views/crm_lead.xml',
    ],
    'installable': True,
    'license': 'GPL-3',
}
