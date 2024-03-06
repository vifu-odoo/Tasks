from odoo import fields, models

class StockPickingBatch(models.Model):
    _name = "stock.picking.batch.dock"
    _description = "Dock"

    name = fields.Char(string="Name")