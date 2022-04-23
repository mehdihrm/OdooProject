from odoo import models, fields, api, _
class ResUsers(models.Model):
    _inherit = 'res.users'
    _description = 'customizing the users so that it will represent patient'

    name=fields.Char(string="name")


    # nom_patient = fields.Char(string="Nom Patient")
    # prenom_patient = fields.Char(string="Prenom Patient")
    # adresse_patient = fields.Char(string="Adresse de Patient")
    # date_naissance = fields.Date(string="Date de Naissance")
    # sexe_patient = fields.Selection(selection=[('f', 'Femme'), ('m', 'Homme')])
    # my_rdvs = fields.One2many("gstrdv.rdvs", "codePatient", string="My Rdvs")

