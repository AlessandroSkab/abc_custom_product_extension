# -*- coding: utf-8 -*-
{
    'name': "product_extension",

    'summary': """
        Editor Html nella descrizione del prodotto""",

    'description': """
        Editor Html nella descrizione del prodotto
    """,

    'author': "ABC Strategie",
    'website': "http://www.abcstrategie.it",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['product','sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/view.xml',
        'report/report.xml',
        'views/view_bis.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}

