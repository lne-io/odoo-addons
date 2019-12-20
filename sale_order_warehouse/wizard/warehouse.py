# -*- coding: utf-8 -*-

from odoo import fields, models, _


class Warehouse(models.TransientModel):
    _name = 'sale_order_warehouse.warehouse'
    _description = 'Set sale order warehouse'

    sale_order_id = fields.Many2one('sale.order', string="Sale order", required=True, readonly=True)
    warehouse_id = fields.Many2one('stock.warehouse', 'Warehouse', required=True)

    def process(self):
        self.sale_order_id.write({'is_warehouse_set': True, 'warehouse_id': self.warehouse_id.id})
        return True