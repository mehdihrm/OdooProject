# -*- coding: utf-8 -*-
# from odoo import http


# class People(http.Controller):
#     @http.route('/people/people', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/people/people/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('people.listing', {
#             'root': '/people/people',
#             'objects': http.request.env['people.people'].search([]),
#         })

#     @http.route('/people/people/objects/<model("people.people"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('people.object', {
#             'object': obj
#         })
