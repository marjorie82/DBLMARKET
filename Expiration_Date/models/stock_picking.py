# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models, SUPERUSER_ID, _, api, fields, models
import logging


_logger = logging.getLogger(__name__)
class StockMovePro(models.Model):
    _inherit = 'stock.move'
    expiration_date = fields.Date('Fecha de Expiracion')


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    @api.model
    def write(self, vals):
        if 'lot_id' in vals:
            lote = self.env['stock.production.lot'].search([('id', '=', vals['lot_id'])])
            lote.write({'life_date':self.expiration_date})
        res = super(StockMoveLine, self).write(vals)
        return res