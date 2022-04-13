from attr import field
from odoo import models, fields, api

class Society(models.Model):
    _inherit='res.partner'
    namespace = fields.Char('NameSpace')