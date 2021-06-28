# -*- coding: utf-8 -*-
# from odoo import http


# class OdooModuleReport(http.Controller):
#     @http.route('/odoo_module_report/odoo_module_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_module_report/odoo_module_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_module_report.listing', {
#             'root': '/odoo_module_report/odoo_module_report',
#             'objects': http.request.env['odoo_module_report.odoo_module_report'].search([]),
#         })

#     @http.route('/odoo_module_report/odoo_module_report/objects/<model("odoo_module_report.odoo_module_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_module_report.object', {
#             'object': obj
#         })
