from odoo import api, fields, models

class StockPickingBatch(models.Model):
    _inherit = "stock.picking.batch"

    dock_id = fields.Many2one('stock.picking.batch.dock', string = "Dock")
    vehicle = fields.Many2one('fleet.vehicle',string = "Vehicle")
    vehicle_category = fields.Many2one('fleet.vehicle.model.category', string = "Vehicle Category")
    weight_progress = fields.Float(string = "Weight", compute = "_compute_volume_weight", store=True)
    volume_progress = fields.Float(string = "Volume", compute = "_compute_volume_weight", store=True)

    total_volume = fields.Float(string = "Total Volume", compute = "_compute_picking_volume_weight")
    total_weight = fields.Float(string = "Total Weight", compute = "_compute_picking_volume_weight")

    transfers = fields.Integer(string="#Transfers", compute = "_compute_transfer", store=True)
    lines = fields.Integer(string="#Lines", compute = "_compute_lines", store=True)

    @api.depends("picking_ids", "vehicle_category")
    def _compute_picking_volume_weight(self):
        for record in self:
            record.total_volume = sum(record.picking_ids.mapped('picking_volume'))
            record.total_weight = sum(record.picking_ids.mapped('picking_weight'))

    @api.depends("picking_ids", "vehicle_category")
    def _compute_volume_weight(self):
        for record in self:
            total_picking_volume = sum(record.picking_ids.mapped('picking_volume'))
            total_picking_weight = sum(record.picking_ids.mapped('picking_weight'))
            
            max_volume = record.vehicle_category.max_volume
            max_weight = record.vehicle_category.max_volume
      
            record.volume_progress = (total_picking_volume / record.vehicle_category.max_volume) * 100 if max_volume > 0 else 0.0
            record.weight_progress = (total_picking_weight / record.vehicle_category.max_weight) * 100 if max_weight > 0 else 0.0 

    @api.depends("picking_ids")
    def _compute_transfer(self):
        for record in self:
            record.transfers = len(record.picking_ids)
    
    @api.depends("move_line_ids")
    def _compute_lines(self):
        for record in self:
            record.lines = len(record.move_line_ids)

    @api.depends("name","total_weight", "total_volume")
    def _compute_display_name(self):
        for record in self:
            formatted_weight = f"{record.total_weight:.2f}"
            formatted_volume = f"{record.total_volume:.2f}"

            record.display_name = (record.name + "(" + formatted_weight + "kg, " + formatted_volume + "m\u00b3)")