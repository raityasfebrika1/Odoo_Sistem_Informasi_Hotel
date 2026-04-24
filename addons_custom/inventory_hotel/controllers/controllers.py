# -*- coding: utf-8 -*-
# from odoo import http


# class InventoryHotel(http.Controller):
#     @http.route('/inventory_hotel/inventory_hotel', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/inventory_hotel/inventory_hotel/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('inventory_hotel.listing', {
#             'root': '/inventory_hotel/inventory_hotel',
#             'objects': http.request.env['inventory_hotel.inventory_hotel'].search([]),
#         })

#     @http.route('/inventory_hotel/inventory_hotel/objects/<model("inventory_hotel.inventory_hotel"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('inventory_hotel.object', {
#             'object': obj
#         })

