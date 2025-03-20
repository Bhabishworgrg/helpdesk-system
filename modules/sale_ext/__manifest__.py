# -*- coding: utf-8 -*-

{
    'name': 'Sale Extension',
    'author': 'Bhabishwor Gurung',
    'category': 'Hidden',
    'depends': [
        'sale',
    ],
    'data': [
        'security/ir.model.access.csv',
        'wizard/sale_order_reject_wizard.xml',
        'views/sale_order.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': True,
    'license': 'GPL-3',
}
