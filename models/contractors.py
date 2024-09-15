from odoo import fields, models


class contractor(models.Model):
    _name = "contractor.unit"
    _description = "Data OF Contractor"

    name = fields.Char(name="name", required=True)
    mobile=fields.Char(name="mobile", required=True)
    phone=fields.Char(name="phone")
    adress=fields.Char(name="adress", required=True)
    info=fields.Char(name="info", required=True)
    image = fields.Binary(string='Photo')
    state = fields.Selection([('good', 'Good'), ('bad', 'Bad')], string="status")

    def project_save(self):
        return True
