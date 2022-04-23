# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class theme(models.Model):
    _name = 'library.theme'
    _description = 'ce modules est destiner pour definir les themes d\'un livre'
    _rec_name = 'theme_code'

    theme_code = fields.Char(string="Id", readonly=True)
    theme_intitule = fields.Char(string="Intitule")

    @api.model
    def create(self, vals):
        if vals.get('theme_code', _('New')) == _('New'):
            vals['theme_code'] = self.env['ir.sequence'].next_by_code('theme_code.sequence') or _('New')
        result = super(theme, self).create(vals)
        return result


class livre(models.Model):
    _name = 'library.livre'
    _description = 'ce modules est destiner pour definir les caracteristiques d\'un livre'
    _rec_name = "lvr_code"

    lvr_code = fields.Char(string="Id", readonly=True)
    lvr_titre = fields.Char(string="Titre")
    lvr_autheur = fields.Char(string="Autheur")
    lve_nbr_pages = fields.Integer(string="Nombre des pages")
    lvr_nbr_exemplaire = fields.Integer(string="Nombre des exemplaire")
    lvr_prix = fields.Float(string="Prix")
    lvr_img = fields.Binary(string="Image")
    lvr_description = fields.Text(string="Description")
    lvr_theme = fields.Many2many("library.theme")

    @api.model
    def create(self, vals):
        if vals.get('lvr_code', _('New')) == _('New'):
            vals['lvr_code'] = self.env['ir.sequence'].next_by_code('livre_code.sequence') or _('New')
        result = super(livre, self).create(vals)
        return result
