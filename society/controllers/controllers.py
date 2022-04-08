# -*- coding: utf-8 -*-
# from odoo import http


# class Society(http.Controller):
#     @http.route('/society/society', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/society/society/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('society.listing', {
#             'root': '/society/society',
#             'objects': http.request.env['society.society'].search([]),
#         })

#     @http.route('/society/society/objects/<model("society.society"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('society.object', {
#             'object': obj
#         })
