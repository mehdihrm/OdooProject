from odoo import models, fields, api, _

class Partner(models.Model):
    _inherit = 'res.partner'

    killMe = fields.Char("Nom", default=False)
    # test_field = fields.Char("test_test_test_test", default="test_test")
    # nom_test = fields.Char(string="Nom Patient")
    # prenom = fields.Char(string="Prenom Patient")
    # adresse = fields.Char(string="Adresse de Patient")
    # datenaissance = fields.Date(string="Date de Naissance")
    # sexe = fields.Selection(selection=[('f', 'Femme'), ('m', 'Homme')])
    # myrdvs = fields.One2many("gstrdv.rdvs", "codePatient", string="My Rdvs")


