# -*- coding: utf-8 -*-
# from odoo import http


# class CooperativaApp(http.Controller):
#     @http.route('/cooperativa_app/cooperativa_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cooperativa_app/cooperativa_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cooperativa_app.listing', {
#             'root': '/cooperativa_app/cooperativa_app',
#             'objects': http.request.env['cooperativa_app.cooperativa_app'].search([]),
#         })

#     @http.route('/cooperativa_app/cooperativa_app/objects/<model("cooperativa_app.cooperativa_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cooperativa_app.object', {
#             'object': obj
#         })
