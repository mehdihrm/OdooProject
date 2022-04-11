# -*- coding: utf-8 -*-

from attr import field
from odoo import models, fields, api


class society(models.Model):
    _name = 'society'
    _description = 'f_society'
    society_name = fields.Char('Name',required=True,readonly=True)
    population = fields.Integer('Age', required=True,readonly=True)

    


    
