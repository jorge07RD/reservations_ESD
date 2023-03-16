from odoo import models, fields

class Specialty(models.Model):
    _name = 'reservations.specialty'
    _description = 'Specialty'

    name = fields.Char(string='Name', required=True)
    area = fields.Char(string='Area', required=True)
