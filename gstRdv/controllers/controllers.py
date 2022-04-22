# -*- coding: utf-8 -*-
# from odoo import http


# class GstRdv(http.Controller):
#     @http.route('/gstRdv/gstRdv', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gstRdv/gstRdv/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gstRdv.listing', {
#             'root': '/gstRdv/gstRdv',
#             'objects': http.request.env['gstRdv.gstRdv'].search([]),
#         })

#     @http.route('/gstRdv/gstRdv/objects/<model("gstRdv.gstRdv"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gstRdv.object', {
#             'object': obj
#         })
