# -*- encoding: utf-8 -*-

{
    'name': 'Set warehouse in sales orders',
    'version': '1.0',
    'category': 'Sales',
    'author': 'lne-io',
    'website': 'https://github.com/lne-io/',
    'summary': "Set warehouse before confirming a sale order.",
    'description': "",
    'depends': ['base', 'stock', 'sale', 'sale_stock'],
    'data': [
        'wizard/warehouse_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}
