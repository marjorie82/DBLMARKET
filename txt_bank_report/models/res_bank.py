# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResBanks(models.Model):
    _inherit = 'res.bank'

    payment_code = fields.Char(string="Codigo para pago electronico")