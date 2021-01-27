# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
from odoo.exceptions import ValidationError


class socios_model(models.Model):
    _name = 'cooperativa_app.socios_model'
    _description = 'cooperativa_app.socios_model'

    id_socio=fields.Integer(string="Id Socio", help="Añade el id del socio",required=True, index=True)
    foto=fields.Binary()
    name = fields.Char(string="Nombre", help="Añade el nombre del socio",required=True)
    apellidos = fields.Char(string="Apellidos", help="Añade los apellidos del socio",required=True)
    dni = fields.Char(string="DNI", help="Añade el dni del socio",required=True)
    fechaAlta = fields.Date(string="Fecha",help="Añade la fecha de alta del socio",required=True,default=datetime.today())
    telf= fields.Char(string="Telefono", help="Añade el telefono del socio", required=True, size=9)
    email = fields.Char(string="email",help="Añade el email del socio")
    saldo = fields.Float(string="Saldo", help="Se actualiza automaticamente", compute="_calcularSaldo", store=True)


    campanya = fields.One2many("cooperativa_app.campanya_model", "socio", string="Campanya")


    @api.constrains("dni")
    def _validarDni(self):
        letras="TRWAGMYFDPXBNJZSQVHLCKE"

        letra =self.dni[-1]
        num=int(self.dni[:-1])
        if letras[num%23]!=letra:
            raise ValidationError ("DNI Invalido!")


    @api.constrains("telf")
    def _validarTelefono(self):
        if len(self.telf)<9:
            raise ValidationError ("Telefono Invalido!")


    @api.constrains("email")
    def is_valid_email(self):
        if "@" not in self.email:
            raise ValidationError("Email Invalido!")
        if len(self.email)<=5:
            raise ValidationError("Email Invalido!")


    @api.depends('saldo')
    def _calcularSaldo(self):
        self.ensure_one()
        
        