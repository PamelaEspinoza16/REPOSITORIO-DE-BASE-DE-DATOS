# -*- coding: utf-8 -*-
# from odoo import http


# class TallerEspinozas(http.Controller):
#     @http.route('/taller__espinozas/taller__espinozas/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/taller__espinozas/taller__espinozas/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('taller__espinozas.listing', {
#             'root': '/taller__espinozas/taller__espinozas',
#             'objects': http.request.env['taller__espinozas.taller__espinozas'].search([]),
#         })

#     @http.route('/taller__espinozas/taller__espinozas/objects/<model("taller__espinozas.taller__espinozas"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('taller__espinozas.object', {
#             'object': obj
#         })
