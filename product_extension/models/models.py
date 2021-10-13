# -*- coding: utf-8 -*-

from odoo import models, fields, api

class product_extension(models.Model):
       _name = 'product_extension.product_extension'
       _description = 'product_extension.product_extension'
    
class ProductTemplate(models.Model):
     _inherit = 'product.template'
#     _description = 'product_extension.product_extension'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
#class SaleOrderLine(models.Model):
#     _inherit = 'sale.order.line'
class SaleOrder(models.Model):
     _inherit = 'sale.order'