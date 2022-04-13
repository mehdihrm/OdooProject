from asyncio.windows_events import NULL
from attr import field
from odoo import models, fields, api
from odoo.exceptions import ValidationError




class society(models.Model):
    _name = 'society.client'
    _description = 'f_society client'

    name = fields.Char('Name',required=True)
    birth_date = fields.Date('Date of birth',required=True)
    phone_number = fields.Char('Phone Number')
    adress = fields.Text('Adress',required=True)
    active = fields.Boolean('Active',default=False)



