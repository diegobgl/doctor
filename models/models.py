# -*- coding: utf-8 -*-

from odoo import models, fields, api

 class doctor(models.Model):
     _name = 'doctor.doctor'

     nombre_doctor = fields.Char(string="Nombre doctor")
     especialidad = fields.Char(string="Especialidad")
