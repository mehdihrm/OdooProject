# -*- coding: utf-8 -*-
# from odoo import http


# class ToUnderstandInheritance(http.Controller):
#     @http.route('/to_understand_inheritance/to_understand_inheritance', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/to_understand_inheritance/to_understand_inheritance/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('to_understand_inheritance.listing', {
#             'root': '/to_understand_inheritance/to_understand_inheritance',
#             'objects': http.request.env['to_understand_inheritance.to_understand_inheritance'].search([]),
#         })

#     @http.route('/to_understand_inheritance/to_understand_inheritance/objects/<model("to_understand_inheritance.to_understand_inheritance"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('to_understand_inheritance.object', {
#             'object': obj
#         })
