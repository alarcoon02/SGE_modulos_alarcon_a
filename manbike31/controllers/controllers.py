# -*- coding: utf-8 -*-
# from odoo import http


# class Manbike31(http.Controller):
#     @http.route('/manbike31/manbike31/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/manbike31/manbike31/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('manbike31.listing', {
#             'root': '/manbike31/manbike31',
#             'objects': http.request.env['manbike31.manbike31'].search([]),
#         })

#     @http.route('/manbike31/manbike31/objects/<model("manbike31.manbike31"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('manbike31.object', {
#             'object': obj
#         })
