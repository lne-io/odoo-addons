# -*- coding: utf-8 -*-
from datetime import datetime
from odoo.tests import common

class TestSale(common.TransactionCase):

    def setUp(self, *args, **kwargs):
        super(TestSale, self).setUp(*args, **kwargs)
        product_uom_id = self.ref('product.product_uom_unit')
        product_id = self.ref('product.product_product_24')
        partner_id = self.ref('base.res_partner_4')
        
        self.warehouse_0_id = self.ref('stock.warehouse0')

        self.sale_order = self.env['sale.order'].create({
            'date_order': datetime.today(),
            'name': 'Test_SO011',
            'order_line': [
                (0, 0, {
                    'name': '[CARD] Individual Workplace',
                    'price_unit': 1000.0,
                    'product_uom': product_uom_id,
                    'product_uom_qty': 10.0,
                    'state': 'draft',
                    'product_id': product_id}
                )
            ],
            'partner_id': partner_id,
            'warehouse_id': self.warehouse_0_id})


    def test_confirm(self):
        "Test state after confim_action"
        # Confirm the sales order.
        self.sale_order.action_confirm()
        
        self.assertEqual("draft", self.sale_order.state, "State should stay draft if warehouse is not set through wizard")
        self.assertEqual(False, self.sale_order.is_warehouse_set, "Is warehouse set should be False if warehouse is not set yet.")

    def test_set_warehouse(self):
        "Test setting warehouse"
        self.warehouse_1 = self.env['stock.warehouse'].create({
            'name': 'Wone',
            'code': 'WO',
        })
        warehouse_wizard = self.env['sale_order_warehouse.warehouse'].create({
            'sale_order_id': self.sale_order.id,
            'warehouse_id': self.warehouse_1.id,
        })

        self.assertEqual(self.warehouse_0_id, self.sale_order.warehouse_id.id, "Sale order warehouse id should equal to the default warehouse")
        warehouse_wizard.process()
        self.assertEqual(self.warehouse_1.id, self.sale_order.warehouse_id.id, "Sale order warehouse id should equal to the new warehouse")
        self.assertEqual(True, self.sale_order.is_warehouse_set, "Is warehouse set should be True after setting warehouse")
        self.sale_order.action_confirm()
        self.assertEqual("sale", self.sale_order.state, "State should be done after setting warehouse")