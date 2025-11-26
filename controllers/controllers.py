# -*- coding: utf-8 -*-
# from odoo import http


# class Excursiones(http.Controller):
#     @http.route('/excursiones/excursiones', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/excursiones/excursiones/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('excursiones.listing', {
#             'root': '/excursiones/excursiones',
#             'objects': http.request.env['excursiones.excursiones'].search([]),
#         })

#     @http.route('/excursiones/excursiones/objects/<model("excursiones.excursiones"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('excursiones.object', {
#             'object': obj
#         })

