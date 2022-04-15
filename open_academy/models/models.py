# -*- coding: utf-8 -*-

from ast import Return, Store
from datetime import datetime, timedelta
from email.policy import default
from odoo import models, fields, api, exceptions


class course (models.Model):
        _name = 'open_academy.course'
        _description = "openAcademy coureses"
        name = fields.Char(string="title", required=True)
        description = fields.Text()
        year = fields.Date()
        photo =fields.Binary()
        responsible_id = fields.Many2one('res.users', ondelete="set null", string='Responsible', index=True)
        session_ids = fields.One2many('openacademy_sessions', 'course_id', string='sisseon')
        
        _sql_constraints = [
                ('name_description_check',
                'CHECK(name!=description)',
                "The title of the course should not be the description"),
                (
                'name_unique',
                'UNIQUE(name)',
                'The course title be unique'
                ),
        ]
        name_seq=fields.Char(default  = lambda self:('New'),readonly=1 )
        @api.model
        def create(self,vals):
                if vals.get('name_seq',('New'))==("New"):
                        vals["name_seq"]=self.env['ir.sequence'].next_by_code('test.course') or('New')
                        delta=super(course,self).create(vals)
                        return delta
        
"""class sessionn"""
class session (models.Model):
        _name = "openacademy_sessions"
        _description = "openAcademy sessions"
        name = fields.Char(string="name")
        startDate = fields.Date(default=fields.Date.today ,string="start date")
        duration = fields.Float(digts=(6, 2), help="Duration in days")
        taken_seats = fields.Float(string="taken seats", compute="_taken_seats")
        endDate= fields.Date(string="End date" ,Store=True ,compute="_get_end_date" , inverse="_set_end_date" ,readonly=1)
        active = fields.Boolean(default=True)
        seats = fields.Integer(string="Number of seats")

        #relations
        instructor_id = fields.Many2one('res.partner', string="instructor")
        course_id = fields.Many2one("open_academy.course", ondelete="cascade", string="course", required=True)
        attendee_ids = fields.Many2many('res.partner', string="Attendees")
        # depends /compute
        @api.depends('seats', 'attendee_ids')
        def _taken_seats(self):
                for record in self:
                        if not record.seats:
                                record.taken_seats = 0.0
                        else:
                                record.taken_seats = 100.0 * \
                                len(record.attendee_ids)/record.seats

        # default value
        # fields.Date.todat => date de system
        
        # onchange
        @api.onchange('seats', 'attendee_ids')
        def verify_valid_steats(self):
                if self.seats < 0:
                        return {
                                'warning': {
                                'title': "Incorrect 'seats' value",
                                'message': 'the number of available seats may not be negative',
                                },
                }

                if len(self.attendee_ids) > self.seats:
                        
                        return {
                                'warning': {
                                'title': "Too many attendes",
                                'message': 'Increase seats or remove excess attemdees',
                                },
                        }
        # python constrains
        @api.constrains('instructor_id', 'attendee_ids')
        def check_instructor_id(self):
                for r in self:
                        if r.instructor_id and r.instructor_id in r.attendee_ids:
                                raise exceptions.ValidationError(
                                'A session instructor can"t be an attendee')
        
        #test bottum
        def test_1(self):
                for r in self:
                        if r.seats and r.seats > 50:
                                raise exceptions.ValidationError(
                                'test LOLOOO')
        #compute/ inverse "endate"
        @api.depends('startDate','duration')
        def _get_end_date(self):
                for r in self:
                        if not (r.startDate and r.duration):
                                r.endDate=r.startDate
                                continue
                        duration=timedelta(days=r.duration,seconds=-1)
                        r.endDate=r.startDate+duration
        def _set_end_date(self):
                for r in self:
                        if not (r.startDate and r.duration):
                                r.endDate=r.startDate
                                continue
                        r.endDate=(r.startDate - r.duration).days+1
