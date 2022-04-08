# -*- coding: utf-8 -*-

from attr import field
from odoo import models, fields, api


class society(models.Model):
    _name = 'society.employee'
    _description = 'f_society employee'

    name = fields.Char('Name',required=True)
    age = fields.Integer('Age', required=True)
    departement = fields.Char('Departement',default='Departement A')
    gender = fields.Selection(selection=[('male','Male'),('female','Female')])
    adress = fields.Text('Adress',required=True)
    salary = fields.Float('Salary',required=True)
    
    active = fields.Boolean('Active',default=False)

