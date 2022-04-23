# -*- coding: utf-8 -*-

from odoo import models, fields, api, Command


class rdv_account(models.Model):
    _inherit='gstrdv.rdvs'

    def generate_invoice(self):
        res = super().generate_invoice()
        journal = self.env["account.journal"].search([("type", "=", "sale")], limit=1)
        # Another way to get the journal:
        # journal = self.env["account.move"].with_context(default_move_type="out_invoice")._get_default_journal()
        for prop in self:
            self.env["account.move"].create(
                {
                    "partner_id": prop.codePatient,
                    "move_type": "out_invoice",
                    "journal_id": journal.id,
                    "invoice_line_ids": [
                        Command.create({
                            "name": prop.codeRdv,
                            "quantity": 1.0, # or champs field
                            "price_unit": 400.00, # or champs field
                        }),
                        Command.create({
                            "name": "Administrative fees",
                            "quantity": 1.0,
                            "price_unit": 100.0,
                        }),
                    ],
                }
            )


# class rdv_account(models.Model):
#     _name = 'rdv_account.rdv_account'
#     _description = 'rdv_account.rdv_account'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
