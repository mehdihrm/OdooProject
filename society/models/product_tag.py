from attr import field
from odoo import models, fields, api


class society(models.Model):
    _name = 'society.product.tag'
    _descirption = 'f_society tag '

    name = fields.Char('Name', required=True)
    color = fields.Integer()
