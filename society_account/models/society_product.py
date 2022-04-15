# -*- coding: utf-8 -*-

from odoo import models, Command,api


class SocietyProduct(models.Model):

    # ---------------------------------------- Private Attributes ---------------------------------

    _inherit = "society.product.sell"

    # ---------------------------------------- Action Methods -------------------------------------

    def confirm_sell(self):
        res = super().confirm_sell()
        
        journal = self.env["account.journal"].search([("type", "=", "sale")], limit=1)
        # Another way to get the journal:
        # journal = self.env["account.move"].with_context(default_move_type="out_invoice")._get_default_journal()
        for prop in self:
            self.env["account.move"].create(
                {
                    "partner_id": prop.client_buyer,
                    "client_id": prop.client_buyer_id,
                    "move_type": "out_invoice",
                    "journal_id": journal.id,
                    "invoice_line_ids": [
                        Command.create({
                            "name": prop.product_id.name,
                            "quantity": prop.product_quantity,
                            "price_unit": prop.product_price,
                        }),
                        Command.create({
                            "name": "Administrative fees",
                            "quantity": 1.0,
                            "price_unit": 10.0,
                        }),
                    ],
                }
            )
        return res


