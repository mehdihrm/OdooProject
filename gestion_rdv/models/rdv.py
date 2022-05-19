from email.policy import default
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import time
import datetime

# class RDV
class rdvs(models.Model):
    _name = "gstrdv.rdvs"
    _description = "this model describes each rdv a Patient can have"
    # _rec_name = "codeRdv"
    codeRdv = fields.Char(string="Code RDV", required=True, readonly=True, index=True, default=lambda self: _('New'),
                          help="this is the code that make each RDV unique")
    codeMedecin = fields.Many2one("gstrdv.medecin", ondelete="set null", string="Medecin")
    codePatient = fields.Many2one("gstrdv.patient", ondelete="set null", string="Patient",
                                  default=lambda self: self.env.user)
    dateRdv = fields.Date(string="Date de RDV", required=True, default=datetime.datetime.now())
    heureRdv = fields.Float(string='Heure de RDV', required=True)

    @api.model
    def create(self, vals):
        if vals.get('codeRdv', _('New')) == _('New'):
            vals['codeRdv'] = self.env['ir.sequence'].next_by_code('gstrdv.rdv.sequence') or _('New')
        result = super(rdvs, self).create(vals)
        return result

    def generate_invoice(self):
        pass



