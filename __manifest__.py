{
    'name': "Operación sujeta a retención",
    'version': '1.0',
    'author': "Fiorentino Francisco",
    'category': 'Contabilidad',
    'depends': ['base', 'l10n_ar'],
    'description': """
    El Módulo agrega la leyenda de "Operación sujeta a retención" en la factura
    si está tildada la opción Operación sujeta a retención en la configuración 
    de la compañía. Se utiliza cuando la empresa tiene irregularidades con afip
    o cuando empieza a facturar.
    """,
    'data': [
        'views/operacion_sujeta_a_retencion_view.xml',
        'views/operacion_sujeta_a_retencion_factura_view.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
