# -*- coding: utf-8 -*-
{
    'name': "Adding Order Priority Field",

    'summary': "Adding a Priority field on quatation, invoice and inventory pages",

    'description': """
Adding a Priority field on quatation, invoice and inventory pages
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale', 'stock', 'account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/sale_order_priority_field.xml',
        'views/stock_picking_priority.xml',
        'views/account_move_priority.xml',
    ],
    # only loaded in demonstration mode
}

