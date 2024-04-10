from odoo import fields, models

class ResCompanyInherited(models.Model):
    _inherit = 'res.company'

    operacion_sujeta_retencion = fields.Boolean(string="Operación sujeta a retención", default=False)

