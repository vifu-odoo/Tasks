from odoo import api, fields, models

class StockPickingBatch(models.Model):
    _inherit = "stock.picking.batch"

    dock_id = fields.Many2one('stock.picking.batch.dock', string = "Dock")
    vehicle = fields.Many2one('fleet.vehicle',string = "Vehicle")
    vehicle_category = fields.Many2one('fleet.vehicle.model.category', string = "Vehicle Category")
    weight_progress = fields.Float(string = "Weight", compute = "_compute_volume_weight", store=True)
    volume_progress = fields.Float(string = "Volume", compute = "_compute_volume_weight", store=True)
    transfers = fields.Integer(string="Transfers", compute = "_compute_transfer", store=True)
    lines = fields.Integer(string="Lines", compute = "_compute_lines", store=True)
    starting_date = fields.Date(default=fields.date.today())
    stoping_date = fields.Date()

    @api.depends("picking_ids", "vehicle_category")
    def _compute_volume_weight(self):
        for record in self:
            total_picking_volume = sum(picking.picking_volume for picking in record.picking_ids)
            total_picking_weight = sum(picking.picking_weight for picking in record.picking_ids)
            
            if record.vehicle_category.max_volume > 0:
                record.volume_progress = (total_picking_volume / record.vehicle_category.max_volume) * 100
            else:
                record.volume_progress = 0.0

            if record.vehicle_category.max_weight > 0:
                record.weight_progress = (total_picking_weight / record.vehicle_category.max_weight) * 100
            else:
                record.weight_progress = 0.0

    @api.depends("picking_ids")
    def _compute_transfer(self):
        for record in self:
            x = len(record.picking_ids)
            record.transfers = x
    
    @api.depends("move_line_ids")
    def _compute_lines(self):
        for record in self:
            x = len(record.move_line_ids)
            record.lines = x