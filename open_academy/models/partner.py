from odoo import models, fields, api
class partner(models.Model):
    _inherit = "res.partner"
    instructor=fields.Boolean("Instructor",default=False)
    session_ids=fields.Many2many('openacademy_sessions',string='Attended session ',redonly=True)

    
