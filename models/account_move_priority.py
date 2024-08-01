from odoo import api, fields, models


# Adding priority field on invoice page------------------------------------------------------------->
class AccountMove(models.Model):
    _inherit = "account.move"

    invoice_priority = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ], string="Priority")
