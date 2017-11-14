# -*- coding: utf-8 -*-

{
    'name': "Altex Contract Report",

    'description': """
        This module to withdraw the certificates
    """,

    'author': "Altex-corp",
    'website': "http://altex-corp.com",

    'version': '1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr','hr_contract'],

    # always loaded
    'data': [
        'report/contract_report.xml',
        'report/contract_report_template.xml',
        'views/altex_contract_view.xml'
    ],
    'installable': True,
}
