from odoo import api, fields, models

class StockPickingBatch(models.Model):
    _name = "stock.picking.batch.dock"

    name = fields.Char(string="Name")