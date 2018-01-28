# -*- coding: utf-8 -*-

from odoo import api, fields, models, SUPERUSER_ID

STATES = [
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

    ]

class Partner(models.Model):

    _inherit = 'res.partner'


    def _default_stage_id(self):
        return self.env['crm.stage'].search([], limit=1).id


    stage_id = fields.Many2one('crm.stage', string='Status', index=True, track_visibility='onchange' , group_expand='_read_group_all_states' , default=lambda self: self._default_stage_id())

    state_contact= fields.Many2one('crm.stage', related='stage_id' ,string='Status', index=True,
         group_expand='_read_group_contact_states', store=True)
    state_target = fields.Many2one('crm.stage', related='stage_id', string='Status', index=True,
         group_expand='_read_group_target_states', store=True)

    state_account = fields.Many2one('crm.stage', related='stage_id', string='Status', index=True,
         group_expand='_read_group_account_states', store=True)

    stage_sequence = fields.Integer(related='stage_id.sequence', string='Status Sequence',   store=True)

    @api.model
    def _read_group_contact_states(self, stages, domain, order):
        search_domain = [('sequence', 'in', (0,1,2,3,4,5,6))]
        stage_ids = stages._search(search_domain, order=order, access_rights_uid=SUPERUSER_ID)
        print('------2---', stage_ids)
        return stages.browse(stage_ids)

    @api.model
    def _read_group_target_states(self, stages, domain, order):
        search_domain = [('sequence', 'in',(6,7,8,9,10,11,12,13))]
        stage_ids = stages._search(search_domain, order=order, access_rights_uid=SUPERUSER_ID)
        print('------2---', stage_ids)
        return stages.browse(stage_ids)

    @api.model
    def _read_group_account_states(self, stages, domain, order):
        search_domain = [('sequence', 'in', (14,15))]
        stage_ids = stages._search(search_domain, order=order, access_rights_uid=SUPERUSER_ID)
        print('------2---', stage_ids)
        return stages.browse(stage_ids)

    @api.model
    def _read_group_all_states(self, stages, domain, order):
        print('------1---')
        #search_domain = [('name', 'in', ('NEVER CONTACTED' ,'ATTEMPT OF CONTACT' ,'PITCHED' ,'CALL BACK' ,'NOT INTERESTED' ,'INTERESTED' ,'OFFER SUBMISSION' ,'MEETING SET' ,'1ST MEETING' ,'2ND MEETING' ,'3RD MEETING' ,'ON HOLD' ,'PRE - AGREEMENT' ,'SIGNED AGREEMENT' ,'ACTIVATED' ,'LOST PAYING'))]
        search_domain = []
        # perform search
        stage_ids = stages._search(search_domain, order=order, access_rights_uid=SUPERUSER_ID)
        print('------2---',stage_ids)
        return stages.browse(stage_ids)





