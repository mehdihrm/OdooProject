# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class gestion_rdv(models.Model):
#     _name = 'gestion_rdv.gestion_rdv'
#     _description = 'gestion_rdv.gestion_rdv'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
