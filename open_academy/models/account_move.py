from odoo import models, fields, api
class account(models.Model):
    _inherit = "account.move"
    user_ids = fields.Many2one(
                'res.users', ondelete="set null", string='users', index=True)

    