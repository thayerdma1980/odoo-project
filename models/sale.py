from odoo import fields, models


class saleinherit(models.Model):
    _inherit = "sale.order"

    dma = fields.Char(name="Project dma")
