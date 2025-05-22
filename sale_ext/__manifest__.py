# -*- coding: utf-8 -*-

{
    'name': 'Sale Extension',
    'summary': 'An extension to Sale module',
    'author': 'Bhabishwor Gurung',
    'category': 'Hidden',
    'depends': [
        'sale',
    ],
    'data': [
        'security/ir.model.access.csv',
        'wizard/sale_order_approve_wizard.xml',
        'wizard/sale_order_reject_wizard.xml',
        'views/sale_order.xml',
    ],
    'installable': True,
    'license': 'MIT',
}
