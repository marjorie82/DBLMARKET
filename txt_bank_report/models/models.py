# -*- coding: utf-8 -*-
import csv
from odoo import models
from odoo.exceptions import UserError


class TxtBankReport(models.AbstractModel):
    _name = 'report.report_csv.vendor_csv_bank'
    _inherit = 'report.report_csv.abstract'

    def generate_csv_report(self, writer, data, payments):
        # writer.writeheader()
        for obj in payments:
            partner = obj.env['res.partner'].browse(obj.partner_id.id)
            bank = partner.bank_ids or partner.parent_id.bank_ids or obj.env['res.partner.bank']
            # if not bank:
            #     raise UserError("El contacto %s no tiene cuenta bancaria" % partner.name)

            writer.writerow({
                '#Cuenta': bank[0].acc_number,
                'Codigo de Banco': bank.bank_id.payment_code,
                'CC': 'CC',
                'proveedor': obj.partner_id.name,
                'C': 'C',
                'monto': obj.amount,
                'codigo de proveedor': obj.partner_id.ref,
                'Pago ACH': 'PAGO ACH'
            })

    def csv_report_options(self):
        res = super().csv_report_options()
        res['fieldnames'].append('#Cuenta')
        res['fieldnames'].append('Codigo de Banco')
        res['fieldnames'].append('CC')
        res['fieldnames'].append('proveedor')
        res['fieldnames'].append('C')
        res['fieldnames'].append('monto')
        res['fieldnames'].append('codigo de proveedor')
        res['fieldnames'].append('Pago ACH')
        res['delimiter'] = ';'
        res['quoting'] = csv.QUOTE_ALL
        return res