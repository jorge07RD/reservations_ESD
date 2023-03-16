from odoo import models, fields, api


class Doctors(models.Model):
    _name = 'reservations.doctors'
    _description = 'doctors'

    name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    identification = fields.Char(string='Identification')
    specialty = fields.Many2one('reservations.specialty', string='Specialty', required=True)
    schedule_start = fields.Datetime(string='Appointment Date start', required=True)
    schedule_end = fields.Datetime(string='Appointment Date end', required=True)
