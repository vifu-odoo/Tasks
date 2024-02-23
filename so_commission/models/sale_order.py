from odoo import models, fields

class SOCommission(models.Model):
    _inherit = 'sale.order'

    so_commission = fields.Boolean(string="Add Commission", default=False)

    #total_commision = fields.Monetary(string="Total Commision", store=True) 
    