from odoo import api, models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    so_commission = fields.Boolean(string="Add Commission", default=False)

    total_commission = fields.Monetary(string="Total Commision", compute='_compute_total_commission', readonly=True) 

    @api.depends('order_line.line_commission')
    def _compute_total_commission(self):
        for order in self:
            order.total_commission = sum(order.order_line.mapped('line_commission'))
    
    @api.depends('order_line.price_subtotal')
    def _compute_amounts(self):
        super()._compute_amounts()
        
        for order in self:
            order.amount_untaxed = sum(line.price_subtotal for line in order.order_line) + order.total_commission
        print("----------------------------------------", order.amount_untaxed)

    # @api.model
    # def create(self, vals):
    #     res = super(SaleOrder, self).create(vals)
    #     # Force recomputation of total_commission and amount_total
    #     res._compute_total_commission()
    #     res._compute_amounts()
    #     return res

       
