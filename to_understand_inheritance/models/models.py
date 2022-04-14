# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class to_understand_inheritance(models.Model):
#     _name = 'to_understand_inheritance.to_understand_inheritance'
#     _description = 'to_understand_inheritance.to_understand_inheritance'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
