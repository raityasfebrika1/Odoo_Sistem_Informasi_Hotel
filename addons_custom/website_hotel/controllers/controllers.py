# -*- coding: utf-8 -*-
# from odoo import http


# class WebsiteHotel(http.Controller):
#     @http.route('/website_hotel/website_hotel', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_hotel/website_hotel/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_hotel.listing', {
#             'root': '/website_hotel/website_hotel',
#             'objects': http.request.env['website_hotel.website_hotel'].search([]),
#         })

#     @http.route('/website_hotel/website_hotel/objects/<model("website_hotel.website_hotel"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_hotel.object', {
#             'object': obj
#         })

