from odoo import api, fields, models


# Adding priority field on inventory page----------------------------------------------------------->
class StockPicking(models.Model):
    _inherit = "stock.picking"

    picking_priority = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ], string='Priority')
