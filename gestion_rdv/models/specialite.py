from email.policy import default

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import time
import datetime


# Specialite_class

class specialite(models.Model):
    _name = "gstrdv.specialite"
    _description = "this model describes each specialite a medecin can have"
    _rec_name = "nomSpecialite"
    # fields related to this class
    codeSpecialite = fields.Char(string="Code de Specialite", required=True, readonly=True, index=True,
                                 default=lambda self: _('New'),
                                 help="this is the code that make each specialite unique")
    nomSpecialite = fields.Char(string="Specialite", required=True)

    @api.model
    def create(self, vals):
        if vals.get('codeSpecialite', _('New')) == _('New'):
            vals['codeSpecialite'] = self.env['ir.sequence'].next_by_code('gstrdv.specialite.sequence') or _('New')
        result = super(specialite, self).create(vals)
        return result
