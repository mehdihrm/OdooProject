# -*- coding: utf-8 -*-
from email.policy import default
from xml.dom.pulldom import default_bufsize
from odoo import models, fields, api, exceptions  

class wizard (models.TransientModel):
        _name = 'openacademy.wizard'
        _description = "wiezatd:Quick regidtration of attendees to sessions"
        
        def _default_sessions(self):
            return self.env['openacademy_sessions'].browse(self._context.get('active_ids'))

        session_ids =fields.Many2many('openacademy_sessions',string='Session',required=True,default=_default_sessions)
        
        attendee_ids =fields.Many2many('res.partner',string='Attendees')

        def subscribe(self):
            for session in self.session_ids:
                session.attendee_ids |= self.attendee_ids
            return{}