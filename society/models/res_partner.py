from attr import field
from odoo import models, fields, api

class Partner(models.Model):
    
    _inherit='account.move'
    
    client_id = fields.Many2one("society.client")
    
