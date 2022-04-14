from odoo import models, fields, api, _

class Partner(models.Model):
    _inherit = 'res.partner'
    killMe = fields.Boolean("Kill Me",default=False)

