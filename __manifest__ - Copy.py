# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Projects DMA',
    'version': '1.0.0.0',
    'summary': 'Projects Apps',
    'sequence': 1,
    'description': """
    From Eng.thayer Bashir  
     """,
    'depends': ['sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/contractor_record.xml',
        'views/location_record.xml',
        'views/project_record.xml',
        'views/sale.xml',
        'views/main_menu.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
