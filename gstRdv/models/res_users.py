from odoo import models, fields, api, _


class ResUsers(models.Model):
    _inherit = 'res.users'

    specialite = fields.One2many("gstrdv.medecin", "Specialite", string="Specialites")
    myname = fields.Char("my name")
