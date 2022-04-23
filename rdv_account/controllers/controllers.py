# -*- coding: utf-8 -*-
# from odoo import http


# class RdvAccount(http.Controller):
#     @http.route('/rdv_account/rdv_account', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rdv_account/rdv_account/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('rdv_account.listing', {
#             'root': '/rdv_account/rdv_account',
#             'objects': http.request.env['rdv_account.rdv_account'].search([]),
#         })

#     @http.route('/rdv_account/rdv_account/objects/<model("rdv_account.rdv_account"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rdv_account.object', {
#             'object': obj
#         })
