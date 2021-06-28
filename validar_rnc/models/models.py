# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from stdnum import do 
from odoo.exceptions import UserError


#Modificaciones en el SaleOrder > Boton indicador de pedido retenido
class CustomerModify(models.Model):
    _inherit = "res.partner"
    def validar_rnc(self):
        if self.name and not self.vat:
            try:
                dgii_info = do.rnc.check_dgii(self.name)    
                if dgii_info:
                    self.name = dgii_info['name']
                    self.vat = dgii_info['rnc']
                else:
                    raise UserError("RNC NO VÁLIDO")
            except:
                raise UserError("SIN RNC")
        else:
            try:    
                dgii_info = do.rnc.check_dgii(self.vat)
                if dgii_info:
                    self.name = dgii_info['name']
                    self.vat = dgii_info['rnc']
                else:
                    raise UserError("RNC NO VÁLIDO")
            except:
                raise UserError("EL RNC ESTABLECIDO ES INCORRECTO")

            

        
    

