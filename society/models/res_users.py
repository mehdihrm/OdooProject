from attr import field
from odoo import models, fields, api

class ResUsers(models.Model):
    
    _inherit='res.users'
    
    product_ids = fields.One2many(
        "society.product", "seller_id", string="Product")
    myname = fields.Char()
    
