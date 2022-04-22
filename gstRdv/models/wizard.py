# from odoo import api, models, fields
# from odoo.exceptions import UserError
# from odoo import exceptions
# import logging
#
# _logger = logging.getLogger(__name__)
#
#
# class SaleConfirmLimit(models.TransientModel):
#     _name = 'sale.control.limit.wizard'
#     invoice_amount = fields.Float('Invoice Amount', readonly=1)
#     new_balance = fields.Float('Total Balance', readonly=1)
#     my_credit_limit = fields.Float('Partner Credit Limit', readonly=1)
#
#
#
#     def agent_exceed_limit(self):
#         _logger.debug(' \n\n \t We can do some actions here\n\n\n')
#
#
