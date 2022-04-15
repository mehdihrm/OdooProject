# -*- coding: utf-8 -*-
from email.policy import default

from odoo import models, fields, api, _
import time


# Medecin_Class

class medecin(models.Model):
    _name = "gstrdv.medecin"
    _description = "this model describes a medecin with define all his personal information and his speciality"
    _rec_name = "codeMedecin"
    # Fields related to this class
    codeMedecin = fields.Char(string="Code Medecin", required=True, readonly=True, index=True,
                              default=lambda self: _('New'), help="this is the code that make each med unique")
    NomMedecin = fields.Char(string="Nom Medecin")
    PrenomMedecin = fields.Char(string="Prenom Medecin")
    TelMedecin = fields.Char(string="Tele de Medecin")
    DateEmbauche = fields.Date(string="Date d'Embauche")
    Specialite = fields.Many2one("gstrdv.specialite", ondelete="set null", string="specialite")
    myRdvs = fields.One2many("gstrdv.rdvs", "codeMedecin", string="My Rdvs")

    @api.model
    def create(self, vals):
        if vals.get('codeMedecin', _('New')) == _('New'):
            vals['codeMedecin'] = self.env['ir.sequence'].next_by_code('gstrdv.medecin.sequence') or _('New')
        result = super(medecin, self).create(vals)
        return result

    # @api.onchange('NomMedecin')
    # def change(self):
    #     print("Hello me")


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

    @api.model
    def create(self, vals):
        if vals.get('codePatient', _('New')) == _('New'):
            vals['codePatient'] = self.env['ir.sequence'].next_by_code('gstrdv.patient.sequence') or _('New')
        result = super(patient, self).create(vals)
        return result


# class RDV
class rdvs(models.Model):
    _name = "gstrdv.rdvs"
    _description = "this model describes each rdv a Patient can have"
    _rec_name = "codeRdv"

    codeRdv = fields.Char(string="RDV", required=True, readonly=True, index=True, default=lambda self: _('New'),
                          help="this is the code that make each RDV unique")
    codeMedecin = fields.Many2one("gstrdv.medecin", ondelete="set null", string="Medecin")
    codePatient = fields.Many2one("gstrdv.patient", ondelete="set null", string="Patient")
    dateRdv = fields.Date(string="Date de RDV", required=True)
    heureRdv = fields.Float(string='Heure de RDV', compute="_compute_time", required=True)

    @api.model
    def create(self, vals):
        if vals.get('codeRdv', _('New')) == _('New'):
            vals['codeRdv'] = self.env['ir.sequence'].next_by_code('gstrdv.rdv.sequence') or _('New')
        result = super(rdvs, self).create(vals)
        return result

    def generate_invoice(self):
        pass

    def _compute_time(self):
        timelocal = time.localtime()
        self.heureRdv = float(time.strftime("%H.%M", timelocal))


# class Maladie

class maladie(models.Model):
    _name = "gstrdv.maladie"
    _description = "this model describes each sickness a Patient can have"
    _rec_name = "nomMaladie"

    codeMaladie = fields.Char(string="Code Maladie", required=True, readonly=True, index=True,
                              default=lambda self: _('New'), help="this is the code that make each Maladie unique")
    nomMaladie = fields.Char(string="Nom Maladie", required=True)
    symptomes = fields.Many2many("gstrdv.symptomes", string="Les Symptomes")

    @api.model
    def create(self, vals):
        if vals.get('codeMaladie', _('New')) == _('New'):
            vals['codeMaladie'] = self.env['ir.sequence'].next_by_code('gstrdv.maladie.sequence') or _('New')
        result = super(maladie, self).create(vals)
        return result


# class Symptomes
class symptomes(models.Model):
    _name = "gstrdv.symptomes"
    _description = "this model describes each symptome a sickness can have"
    _rec_name = "nomSymptomes"

    id = fields.Char(string="Code Symptome", required=True, readonly=True, index=True,
                     default=lambda self: _('New'), help="this is the code that make each Symptome unique")

    codeSymptome = fields.Char(string="Code Symptome", required=True, readonly=True, index=True,
                               default=lambda self: _('New'), help="this is the code that make each Symptome unique")
    nomSymptomes = fields.Char(string="Nom Symptomes", required=True)
    maladieLst = fields.Many2many("gstrdv.maladie", string="Les Maladies")

    @api.model
    def create(self, vals):
        if vals.get('codeSymptome', _('New')) == _('New'):
            vals['codeSymptome'] = self.env['ir.sequence'].next_by_code('gstrdv.symptomes.sequence') or _('New')
        if vals.get('id', _('New')) == _('New'):
            vals['id'] = self.env['ir.sequence'].next_by_code('gstrdv.symptomes.sequence') or _('New')

        result = super(symptomes, self).create(vals)
        return result







# @api.constrains('nomSymptomes')
# def chack_to_validate(self):
#     print(len(self))

# self is a set of records that are in use currrently

# @api.ondelete(at_uninstall=False)
# def check(self):
#     print(len(self))
