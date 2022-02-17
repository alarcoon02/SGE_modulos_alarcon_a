# -*- coding: utf-8 -*-

from odoo import models, fields, api


class manbike31(models.Model):
    _name = 'manbike31.manbike31'
    _description = 'manbike31.manbike31'

    name = fields.Char()
    description = fields.Text()
    price = fields.Float()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
