from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    order_priority = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ], string='Priority')

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        self._update_picking_priorities()

    def _update_picking_priorities(self):
        """
        Here we try to find the partner_id field that present on stock_picking model
        and check it with partner_id field on quotation model, so we get the corresponding quotation.
        hence we update the picking_priority field with quotation order_priority on quotation model
        """
        for order in self:
            pickings = self.env["stock.picking"].search([
                ("partner_id", "=", order.partner_id.id)  # when using many2one field in search domain (order.partner_id) we need to use extra 'id' to get numeric id
            ])
            pickings.write({"picking_priority": order.order_priority})

    def _prepare_invoice(self):
        invoice_vals = super()._prepare_invoice()
        invoice_vals['invoice_priority'] = self.order_priority
        return invoice_vals
