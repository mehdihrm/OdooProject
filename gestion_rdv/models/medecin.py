from email.policy import default

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import time
import datetime


# Medecin_Class

class medecin(models.Model):
    _name = "medecin"
    _description = "this model describes a doctor and define all his personal information and his speciality"
    _rec_name = "codeMedecin"
    # Fields related to this class
    codeMedecin = fields.Char(string="Code Medecin", required=True, readonly=True, index=True,
                              default=lambda self: _('New'), help="this is the code that make each med unique")
    NomMedecin = fields.Char(string="Nom Medecin")
    PrenomMedecin = fields.Char(string="Prenom Medecin")
    TelMedecin = fields.Char(string="Tele de Medecin")
    DateEmbauche = fields.Date(string="Date d'Embauche")
    AnneeActive = fields.Integer(string="Annee Active", compute='_calculer_an_active', readonly=True)
    Specialite = fields.Many2one("gstrdv.specialite", ondelete="set null", string="specialite")
    myRdvs = fields.One2many("gstrdv.rdvs", "codeMedecin", string="My Rdvs")
    myRdvs_count = fields.Integer(string="CommeBien des RDV ai-je?!", compute='count_rdv_per_medecin', store=True)

    @api.model
    def create(self, vals):
        if vals.get('codeMedecin', _('New')) == _('New'):
            vals['codeMedecin'] = self.env['ir.sequence'].next_by_code('gstrdv.medecin.sequence') or _('New')
        result = super(medecin, self).create(vals)
        return result

    # @api.depends('DateEmbauche')
    def _calculer_an_active(self):
        for record in self:
            if record.DateEmbauche:
                year = datetime.datetime.strptime(str(record['DateEmbauche']), "%Y-%m-%d").strftime("%Y")
                record.AnneeActive = datetime.datetime.now().year - int(year)

    @api.depends('myRdvs')
    def count_rdv_per_medecin(self):
        for record in self:
            record.myRdvs_count = len(record.myRdvs)
