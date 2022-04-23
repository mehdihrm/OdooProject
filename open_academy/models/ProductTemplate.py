from odoo import models, fields, api
class partner(models.Model):
    _inherit = "res.partner"
    instructor=fields.Boolean("Instructor",default=False)

    
