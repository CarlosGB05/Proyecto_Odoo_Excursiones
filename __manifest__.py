#-- coding: utf-8 --
{
    'name': "Gestión de Excursiones Escolares",

    'summary': "Módulo para planificar excursiones escolares, destinos y profesores responsables.",

    'description': """
    Permite gestionar excursiones, destinos y profesores encargados de las salidas escolares.
    """,

    'author': "Mahou",
    'website': "https://www.mahou.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'reports/excursion_report.xml',
        'views/views.xml',
        'views/templates.xml',
    ],

    'application': True,
    'installable': True,
    'auto_install': False,
    # only loaded in demonstration mode
    'demo': [],
}

