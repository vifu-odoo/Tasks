from odoo import api, fields, models

class StockPicking(models.Model):
    _inherit = "stock.picking"

    picking_weight = fields.Float(string = "Weight", compute="_compute_weight_volume")
    picking_volume = fields.Float(string = "Volume", compute="_compute_weight_volume")

    @api.depends("move_ids", "move_ids.product_id", "move_ids.quantity")
    def _compute_weight_volume(self):
        for record in self:
            total_volume = 0.0
            total_weight = 0.0
            for line in record.move_ids:
                total_volume += line.product_id.volume * line.quantity
                total_weight += line.product_id.weight * line.quantity
            record.picking_volume = total_volume
            record.picking_weight = total_weight