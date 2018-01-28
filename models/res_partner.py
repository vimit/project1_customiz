# -*- coding: utf-8 -*-

from odoo import api, fields, models, SUPERUSER_ID

class Partner(models.Model):

    _inherit = 'res.partner'

    state = fields.Selection([
        ('never-contacted','NEVER CONTACTED'),
        ('attempt-contact','ATTEMPT OF CONTACT'),
        ('pitched','PITCHED'),
        ('call-back','CALL BACK'),
        ('not-interested','NOT INTERESTED'),
        ('interested','INTERESTED'),
        ('offer','OFFER SUBMISSION'),
        ('meeting','MEETING SET'),
        ('1meeting','1ST MEETING'),
        ('2meeting','2ND MEETING'),
        ('3meeting','3RD MEETING'),
        ('hold','ON HOLD'),
        ('pre-agreement','PRE - AGREEMENT'),
        ('signed','SIGNED AGREEMENT'),
        ('activated','ACTIVATED'),
        ('lost-paying','LOST PAYING')

    ], string='Status', index=True,  default='never-contacted',
        track_visibility='onchange')