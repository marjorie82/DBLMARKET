# -*- coding: utf-8 -*-
{
    'name': "VALIDAR RNC",

    'summary': """
        - Validacion de RNC Republica Dominicana""",

    'description': """
        - Validacion de RNC Republica Dominicana
    """,

    'author': "Hector Contreras",
    'website': "growit.com.do",

    'category': 'Set',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
