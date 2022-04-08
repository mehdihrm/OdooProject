# -*- coding: utf-8 -*-

from odoo import models, fields, api


class people(models.Model):
    _name = 'people.people'
    _description = 'people.people'

    name = fields.Char(string="Name", required=True, help='we would like to know your name', index=True)
    age = fields.Char(string="Age", required=True, help='we would like to know your age', index=True)
    city = fields.Char(string="City", required=False, help='we would like to know your city', index=True)


    #value = fields.Integer()
    #value2 = fields.Float(compute="_value_pc", store=True)
    #description = fields.Text()

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
