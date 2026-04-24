# -*- coding: utf-8 -*-
# from odoo import http


# class FrontOffice(http.Controller):
#     @http.route('/front_office/front_office', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/front_office/front_office/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('front_office.listing', {
#             'root': '/front_office/front_office',
#             'objects': http.request.env['front_office.front_office'].search([]),
#         })

#     @http.route('/front_office/front_office/objects/<model("front_office.front_office"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('front_office.object', {
#             'object': obj
#         })

