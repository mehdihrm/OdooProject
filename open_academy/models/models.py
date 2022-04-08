#-*- coding: utf-8 -*-

from odoo import models,fields
class course (models.Model):
        _name = 'open_academy.course'
        _description = "openAcademycoureses"
        name = fields.Char(string="title" , required=True)
        description = fields.Text()
        year= fields.Date()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
