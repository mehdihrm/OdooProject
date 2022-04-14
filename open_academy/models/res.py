import random
from odoo import models, fields, api


class partenr (models.Model):
    _inherit = "res.partner"
    age = fields.Char()


"""
class ComputedModel(models.Model):
    _name = 'test.computed'
    name = fields.Char(compute='_compute_name1')
    value = fields.Integer()
    def _compute_name1(self):
        for record in self:
            record.name = str(random.randint(1, 1e6))


dependecies 2 fields con
class TestComputed(models.Model):
    _name = "test.computed"

    total = fields.Float(compute="_compute_name1")
    amount = fields.Float()

    @api.depends("amount")
    def _compute_total(self):
        for record in self:
            record.total = 2.0 * record.amount"""
