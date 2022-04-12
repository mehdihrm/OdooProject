from attr import field
from odoo import models, fields, api

class society(models.Model):
    _name = 'society.product'
    _description = 'f_society product'
    tag = fields.Many2many("society.product.tag")
    name = fields.Char('Product name',required=True)
    category = fields.Selection(selection = [('phone','Phone'),('computer','Computer'),('smarttv','SmartTv')])
    price = fields.Float('Price',required=True)
    active = fields.Boolean('Active',default=False)
    seller_id = fields.Many2one("society.employee",string="Seller")

def getPrice(self):
    return self.price