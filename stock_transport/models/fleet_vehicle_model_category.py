from odoo import api, fields, models

class FleetVehicleModelCategory(models.Model):
    _inherit = 'fleet.vehicle.model.category'

    max_weight = fields.Float(string = "Max Weight (Kg)")
    max_volume = fields.Float(string = "Max Volume (m\u00b3)")

    @api.depends('max_weight', 'max_volume')
    def _compute_display_name(self):
        for record in self:
            name = record.name
            if record.max_weight or record.max_volume:
                name = f"{name} ({record.max_weight}kg, {record.max_volume}m\u00b3)"
            record.display_name = name