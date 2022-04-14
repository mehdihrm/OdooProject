from random import randint
from attr import field
from odoo import models, fields, api

class society(models.Model):
    _name = 'society.product'
    _description = 'f_society product'
    _rec_name="name"
    tag = fields.Many2many("society.product.tag")
    name = fields.Char('Product name',required=True)
    category = fields.Selection(selection = [('phone','Phone'),('computer','Computer'),('smarttv','SmartTv')])
    price = fields.Float('Price',required=True)
    active = fields.Boolean('Active',default=False)
    seller_id = fields.Many2one("res.users", string="Salesman", default=lambda self: self.env.user)
    _sql_constraints = [
        ('check_price', 'CHECK(price > 0)',
         'The product quantity must be superior to 0')
    ]


def getPrice(self):
    return self.price