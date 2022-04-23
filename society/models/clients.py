from attr import field
from odoo import models, fields, api

class Society(models.Model):
    _name = 'society.clients'
    _inherits={'res.partner' : 'related_client_id'}
    _description = 'f_society client'



    name = fields.Char('Name',required=True)
    user_id = fields.Many2one('res.users','Related user')

    client_id = fields.Many2one('society.client','Related Client')
    related_client_id = fields.Many2one('society.client','Related Client ID')






    