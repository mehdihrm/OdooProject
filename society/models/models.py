# -*- coding: utf-8 -*-

from attr import field
from odoo import models, fields, api


class society(models.Model):
    _name = 'society.employee'
    _description = 'f_society employee'

    name = fields.Char('Name',required=True)
    age = fields.Integer('Age', required=True)
    phone_number = fields.Char('Phone Number')

    departement = fields.Char('Departement',default='Departement A')
    
    gender = fields.Selection(selection=[('male','Male'),('female','Female')])
    adress = fields.Text('Adress',required=True)
    salary = fields.Float('Salary',required=True)
    
    active = fields.Boolean('Active',default=False)
    status = fields.Selection(selection = [('new','New'),('manager','Manager'),('Chief','chief')])

class society(models.Model):
    _name = 'society.client'
    _description = 'f_society client'

    name = fields.Char('Name',required=True)
    birth_date = fields.Date('Date of birth',required=True)
    phone_number = fields.Char('Phone Number')
    adress = fields.Text('Adress',required=True)
    active = fields.Boolean('Active',default=False)

class society(models.Model):
    _name = 'society'
    _description = 'f_society'
    society_name = fields.Char('Name',required=True,readonly=True)
    population = fields.Integer('Age', required=True,readonly=True)
   

class society(models.Model):
    _name = 'society.product'
    _description = 'f_society product'
    tag = fields.Many2many("society.product.tag")
    name = fields.Char('Product name',required=True)
    category = fields.Selection(selection = [('phone','Phone'),('computer','Computer'),('smarttv','SmartTv')])
    price = fields.Float('Price',required=True)
    active = fields.Boolean('Active',default=False)
    seller_id = fields.Many2one("society.employee",string="Seller")

class society(models.Model):
    _name = 'society.product.tag'
    _descirption = 'f_society tag'

    name = fields.Char('Name',required=True)

    


    
