# -*- coding: utf-8 -*-
# from odoo import http


# class GestionRdv(http.Controller):
#     @http.route('/gestion_rdv/gestion_rdv', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestion_rdv/gestion_rdv/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestion_rdv.listing', {
#             'root': '/gestion_rdv/gestion_rdv',
#             'objects': http.request.env['gestion_rdv.gestion_rdv'].search([]),
#         })

#     @http.route('/gestion_rdv/gestion_rdv/objects/<model("gestion_rdv.gestion_rdv"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestion_rdv.object', {
#             'object': obj
#         })
