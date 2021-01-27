# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class productos_model(models.Model):
    _name = 'cooperativa_app.productos_model'
    _description = 'cooperativa_app.productos_model'


    name = fields.Char(string="Nombre", help="Añade el nombre del producto",required=True)
    descripcion = fields.Html(string="Descripcion", help="Añade la descripcion del producto",required=True)
    precio = fields.Float(string="Precio", help="añade el precio del producto", required=True)
    kilosTotales = fields.Float(string="Kilos Totales", help="añade el precio del producto", compute="_calcularKilosTotales", store=True)


    @api.constrains("precio")
    def _validarPrecio(self):
        if self.precio<0:
            raise ValidationError ("El precio tiene que ser mayor que 0!")

    @api.depends('kilosTotales')
    def _calcularKilosTotales(self):
        self.ensure_one()




    def limpiaKilos(self):
        self.ensure_one()
        for i in self.kilosTotales:
            i=0


