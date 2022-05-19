from email.policy import default

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import time
import datetime


# Patient_class

class patient(models.Model):
    _name = "gstrdv.patient"
    _description = "this model describes each caracter a Patient can have"
    # _inherits = {'res.partner' : 'codePatient'}
    _rec_name = "codePatient"
    # fields related to this class
    codePatient = fields.Char(string="Code Patient", required=True, readonly=True, index=True,
                              default=lambda self: _('New'), help="this is the code that make each Patient unique")
    nomPatient = fields.Char(string="Nom Patient")
    prenomPatient = fields.Char(string="Prenom Patient")
    adressePatient = fields.Char(string="Adresse de Patient")
    dateNaissance = fields.Date(string="Date de Naissance")
    sexePatient = fields.Selection(selection=[('f', 'Femme'), ('m', 'Homme')])
    myRdvs = fields.One2many("gstrdv.rdvs", "codePatient", string="My Rdvs")
    my_rdv_count = fields.Float(string="commebien des rdv j'assiste?!", compute="_pers_rdvs",
                                inverse="_pers_rdvs_inverse")

    @api.model
    def create(self, vals):
        if vals.get('codePatient', _('New')) == _('New'):
            vals['codePatient'] = self.env['ir.sequence'].next_by_code('gstrdv.patient.sequence') or _('New')
        result = super(patient, self).create(vals)
        return result

    @api.depends('myRdvs')
    def _pers_rdvs(self):
        for record in self:
            if record.myRdvs:
                record.my_rdv_count = 100.0 * len(record.myRdvs) / 50
            else:
                record.my_rdv_count = 0.00

    @api.depends('myRdvs')
    def _pers_rdvs_inverse(self):
        for record in self:
            if record.myRdvs:
                record.my_rdv_count = 50 * len(record.myRdvs) / 100.0