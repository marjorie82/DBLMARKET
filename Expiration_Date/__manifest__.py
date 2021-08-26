# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': "Expiration Date Support",
    'summary': 'This module give support to write the expiration date',
    'description': """This module give support to write the expiration date, on the next modules:
    Purchase.
    Transfer.""",
    'category': 'Stock',
    'depends': ['stock'],
    'sequence': 25,
    'data': [
        'views/stock_picking_exp_date.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'author': 'DIEGO HIDALGO D.',
    'website': "https://www.oikoschain.com",
    'company': 'OikosChain, SRL',
    'maintainer': 'OikosChain, SRL',


}
