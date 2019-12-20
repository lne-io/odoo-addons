# -*- encoding: utf-8 -*-
import logging
from odoo import api, fields, models, _

_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = "sale.order"

    is_warehouse_set = fields.Boolean('Is warehouse set', default=False, readonly=True, help="If false show a wizard to tell the user to choose a warehouse")

    @api.multi
    def action_confirm(self):
        for order in self:
            if not order.is_warehouse_set:
                view = self.env.ref('sale_order_warehouse.view_set_warehouse')
                wiz = self.env['sale_order_warehouse.warehouse'].create({'sale_order_id': order.id, 'warehouse_id': order.warehouse_id.id})
                return {
                    'name': _('Set warehouse'),
                    'type': 'ir.actions.act_window',
                    'view_type': 'form',
                    'view_mode': 'form',
                    'res_model': 'sale_order_warehouse.warehouse',
                    'views': [(view.id, 'form')],
                    'view_id': view.id,
                    'target': 'new',
                    'res_id': wiz.id,
                    'context': self.env.context,
                }
        return super(SaleOrder, self).action_confirm()
        

    