# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
from datetime import date

class Profesor(models.Model):
    _name = 'excursiones.profesor'
    _description = 'Define los atributos de un profesor'
    _rec_name = 'nombre'

    nombre = fields.Char(string='Nombre', required=True)
    email = fields.Char(string='Correo electrónico')
    telefono = fields.Char(string='Teléfono')
    departamento = fields.Char(string='Departamento')
    rol = fields.Selection([
        ('coordinador', 'Coordinador'),
        ('acompanante', 'Acompañante'),
        ('apoyo', 'Apoyo')
    ], string='Rol en excursión', default='acompanante')

    excursiones_ids = fields.One2many('excursiones.excursion', 'profesor_id', string='Excursiones')

class Destino(models.Model):
    _name = 'excursiones.destino'
    _description = 'Define los atributos de un destino de excursión'
    _rec_name = 'nombre'

    nombre = fields.Char(string='Nombre', required=True)
    direccion = fields.Char(string='Dirección')
    contacto = fields.Char(string='Persona de contacto')
    telefono = fields.Char(string='Teléfono')
    email = fields.Char(string='Correo electrónico')
    tipo = fields.Selection([
        ('cultural', 'Cultural'),
        ('natural', 'Natural'),
        ('recreativo', 'Recreativo'),
        ('educativo', 'Educativo')
    ], string='Tipo de destino')
    descripcion = fields.Text(string='Descripción')
    coste_entrada = fields.Float(string='Coste entrada por alumno (€)', digits=(10, 2))

    excursiones_ids = fields.One2many('excursiones.excursion', 'destino_id', string='Excursiones')

class Excursion(models.Model):
    _name = 'excursiones.excursion'
    _description = 'Define los atributos de una excursión escolar'
    _rec_name = 'nombre'

    nombre = fields.Char(string='Nombre de la excursión', required=True)
    fecha = fields.Date(string='Fecha', required=True, default=fields.Date.today)
    hora_salida = fields.Datetime(string='Hora de salida')
    hora_regreso = fields.Datetime(string='Hora de regreso')
    curso = fields.Char(string='Curso participante')
    transporte = fields.Char(string='Transporte')
    
    profesor_id = fields.Many2one('excursiones.profesor', string='Profesor responsable')
    destino_id = fields.Many2one('excursiones.destino', string='Destino')
    

    @api.constrains('fecha')
    def _check_fecha(self):
        hoy = date.today()
        for excursion in self:
            if (excursion.fecha < hoy):
                raise exceptions.ValidationError(" La fecha de la excursión debe ser igual o posterior a hoy.")

