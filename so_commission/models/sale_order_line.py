from odoo import fields, models

class SaleOrderLineSOComm(models.Model):
    _inherit = 'sale.order.line'

    line_commission = fields.Integer(string="Commission")