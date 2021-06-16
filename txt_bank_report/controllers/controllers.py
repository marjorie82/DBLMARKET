# -*- coding: utf-8 -*-
# from odoo import http


# class Addons/txtBankReport(http.Controller):
#     @http.route('/addons/txt_bank_report/addons/txt_bank_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/addons/txt_bank_report/addons/txt_bank_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('addons/txt_bank_report.listing', {
#             'root': '/addons/txt_bank_report/addons/txt_bank_report',
#             'objects': http.request.env['addons/txt_bank_report.addons/txt_bank_report'].search([]),
#         })

#     @http.route('/addons/txt_bank_report/addons/txt_bank_report/objects/<model("addons/txt_bank_report.addons/txt_bank_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('addons/txt_bank_report.object', {
#             'object': obj
#         })
