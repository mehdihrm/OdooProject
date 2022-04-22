from odoo import models, fields, api, _


class Partner(models.Model):
    _name = "res.partner"
    _inherit = "res.partner"

    desc_Text = fields.Char(string="Description", help="we want to know smthing about you")
    candy_fld = fields.Integer(string="How Much Do You Love Candy?")

