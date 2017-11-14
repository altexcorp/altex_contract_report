# -*- coding: utf-8 -*-

from openerp import models , fields , api , _ , tools

class Hr_Employee(models.Model):

    _inherit = 'hr.employee'

    soussigne = fields.Many2one('hr.employee', 'Soussigne')
    date_signature = fields.Date('Date du Signature' , default=fields.Datetime.now)
    type = fields.Selection([('indeterminee', 'Indéterminée'), ('determinee', 'Déterminée'), ('other', 'Other')], 'Type de contrat')

class Hr_contract(models.Model):

    _inherit = 'hr.contract'


