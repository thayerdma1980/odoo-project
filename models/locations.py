from odoo import fields, models


class sites(models.Model):
    _name = "location.unit"
    _description = "Data OF site"

    name = fields.Char(name="Locaion Name", required=True)
    info=fields.Char(name="info")
