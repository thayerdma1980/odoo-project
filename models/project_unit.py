from odoo import fields, models


class project(models.Model):
    _name = "project.unit"
    _description = "Data OF Projct"

    name = fields.Char(name="Project Name", required=True)
    contractor=fields.Many2one('contractor.unit',name="Contracor",required=True)
    location=fields.Many2one('location.unit',name="Location",required=True)
    state=fields.Selection([('actived','In Process'),('finished','Finished'),('archive','Archive')])
    def project_save(self):
        return True