# -*- coding: utf-8 -*-
{
    'name': "society",

    'summary': """ 
        F Society Hackers Group
    """,

    'description': """
        Managing f_society
    """,

    'author': "Robot",
    'website': "http://www.fsociety.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web', 'account'],

    # always loaded
    'data': [
        'security/security.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/employee.xml',
        'views/client.xml',
        'views/product.xml',
        'views/product_tag.xml',
        'views/user_view.xml',
        'views/account_view.xml',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}
