from odoo import api, models, fields

class SOCommission(models.Model):
    _inherit = 'sale.order'

    so_commission = fields.Boolean(string="Add Commission", default= False)

    