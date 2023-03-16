from random import randint
from odoo import models, fields, api
from odoo.exceptions import UserError


class reservations(models.Model):
    _name = 'reservations.reservations'
    _description = 'reservations.reservations'

    code = fields.Char(string='Code', readonly=True, copy=False, index=True, default=lambda self: self.generate_random_code())
    name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    identification = fields.Char(string='Identification', required=True)
    doctor_id = fields.Many2one('reservations.doctors', string='Doctor', copy=False)
    appointment_date = fields.Datetime(string='Appointment Date', copy=False)
    MEDICAL_INSURANCE_OPTIONS = [
        ('Palic', 'ARS Palic'),
        ('Humano', 'ARS Humano'),
        ('Universal', 'ARS Universal'),
        ('Monumental', 'ARS Monumental'),
        ('Futuro', 'ARS Futuro'),
        ('Renacer', 'ARS Renacer'),
        ('Seguro Nacional de Salud', 'Seguro Nacional de Salud'),
        ('Semma', 'ARS Semma'),
        ('Meta Salud', 'ARS Meta Salud'),
        ('Reservas', 'ARS Reservas'),
        ('Siempreviva', 'ARS Siempreviva'),
    ]

    medical_insurance = fields.Selection(MEDICAL_INSURANCE_OPTIONS, string='Medical Insurance')
    comment = fields.Text(string='Comment')

    @api.constrains('doctor_id', 'date_time')
    def _check_reservation(self):
        for rec in self:
            is_reservations = self.search([('id', '!=', rec.id),
                                           ('doctor_id', '=', rec.doctor_id.id),
                                           ('appointment_date', '=', rec.appointment_date)])
            if is_reservations:
                raise UserError('Doctor already has a reservation at that time.')

    @api.constrains('appointment_date', 'doctor_id')
    def _check_appointment_date(self):
        for record in self:
            doctor = record.doctor_id
            if doctor:
                if record.appointment_date < doctor.schedule_start or\
                    record.appointment_date > doctor.schedule_end:
                    raise UserError("You cannot book an appointment outside of the doctor's working hours.")

    def generate_random_code(self):
        """Generates an 8-digit code for the reservation."""
        code = randint(10000000, 99999999)
        return code
