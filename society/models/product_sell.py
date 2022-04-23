from attr import field
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import datetime,timedelta

class society(models.Model):
    _name = 'society.product.sell'
    _description = 'f_society products sells'
    _order = "id desc"

    name = fields.Char()
    state = fields.Boolean("state",default=True,readonly=True)
    product_id = fields.Many2one("society.product",string="Product Name")
    product_price = fields.Float("Price")
    client_buyer = fields.Many2one("res.partner",string="Buyer")
    client_buyer_id = fields.Many2one("society.client",string="Buyer ID")
    product_quantity = fields.Integer('Quantity')
    delivery_date = fields.Date('Expected delivery date :',compute="_get_del_date",inverse="_inverse_get_del_date")
    sold = fields.Boolean(default=False)

    total = fields.Float("Total Price",compute="_get_total_price")
    line_ids = fields.One2many("product.sell.line", "model_id")

    _sql_constraints = [
        ('check_quantity', 'CHECK(product_quantity > 0)',
         'The product quantity must be superior to 0')
    ]

    @api.onchange('product_id')
    def onchange_product(self):
        self.product_price = self.product_id.price
        

    @api.depends('product_price','product_quantity')
    def _get_total_price(self):
        for record in self:
            record.total = record.product_price * record.product_quantity

    def cancel_deal(self):
        for record in self:
            if record.state == True:
                record.state = False
            else:
                raise ValidationError("This deal is already canceled.")
        return True

    def activate_deal(self):
        for record in self:
            if record.state == False:
                record.state = True
            else:
                raise ValidationError("This deal is already activated.")
        return True

    @api.constrains('delivery_date')
    def _check_date_end(self):
        for record in self:
            if record.delivery_date:
                if record.delivery_date < fields.Date.today():
                    raise ValidationError("The delivery date cannot be set in the past")
    
    def _get_del_date(self):
        current_date = datetime.now().date()
        new_date = current_date + timedelta(days=7)
        for record in self:
            record.delivery_date = new_date

    def _inverse_get_del_date(self):
        current_date = datetime.now().date()
        new_date = current_date - timedelta(days=7)
        for record in self:
            new_date = record.delivery_date

    def unlink(self):
        for record in self:
            if record.state == True:
                    raise ValidationError("The record must be cancled before deleting it")
        return super(society,self).unlink()

    def confirm_sell(self):
        for record in self:
            if record.state == False:
                raise ValidationError("The record must be active before confirming the sale")
            else:
                record.sold = True
        return True



class ProductSellLine(models.Model):
    _name="product.sell.line"
    _description = "Test model line"

    model_id = fields.Many2one("society.product.sell")
    field_1 = fields.Char()
    field_2 = fields.Char()
    field_3 = fields.Char()

    





