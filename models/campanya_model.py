# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime


class campanya_model(models.Model):
    _name = 'cooperativa_app.campanya_model'
    _description = 'cooperativa_app.campanya_model'

    fecha = fields.Datetime(string="Fecha", help="Añade la fecha y la hora", required=True, index=True, default=lambda self: datetime.now())
    #campanya = fields.Date(string="Campaña", help="Añade el año de la campanya", default=datetime.year())
    #producto = fields.Float(string="Precio", help="añade el precio de la campanya")
    kilos = fields.Float(string="Kilos Totales", help="añade los kilos de la campanya")


    socio = fields.Many2one("cooperativa_app.socios_model", string="Socios")
