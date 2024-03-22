#-*- coding: utf-8 -*-


# import itertools
# import string
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class taller__espinozas(models.Model):
    _name = 'taller__espinozas.taller__espinozas'
    _description = 'taller__espinozas.taller__espinozas'

    name = fields.Char(string="producto")
    value = fields.Integer()



class Producto(models.Model):
    _name = 'mi_modulo.producto'

    # name = fields.Char(string="ID de producto", compute='_compute_product_id', store=True)
    name = fields.Char(string="Nombre del Producto")
    # @api.depends('id')
    # def _compute_product_id(self):
    #     for product in self:
    #         letters = string.ascii_uppercase
    #         number_range = range(1, len(self) + 1)
    #         number_combinations = itertools.product(letters, number_range)
    #         product.name = ''.join(next(number_combinations))
            
    cantidad = fields.Integer(string="Cantidad")
    precio = fields.Float(string="Precio")
    proveedor_id = fields.Many2one('mi_modulo.proveedor', string="Proveedor")

    proveedor_nombre = fields.Char(string="Nombre del Proveedor", compute='_compute_proveedor_nombre')

    @api.depends('proveedor_id')
    def _compute_proveedor_nombre(self):
        for producto in self:
            producto.proveedor_nombre = producto.proveedor_id.nombre if producto.proveedor_id else ''



class Proveedor(models.Model):
    _name = 'mi_modulo.proveedor'

    nombre = fields.Char(string="Nombre")
    telefono = fields.Char(string="Teléfono")
    direccion = fields.Text(string="Dirección")



class Venta(models.Model):
    _name = 'mi_modulo.venta'

    # producto_id = fields.Many2one('mi_modulo.producto', string="Producto")
    # cantidad = fields.Integer(string="Cantidad")
    producto_id = fields.Many2one('mi_modulo.producto', string="Producto", required=True)
    cantidad = fields.Integer(string="Cantidad", required=True)

    def action_registrar_venta(self):
        for venta in self:
            producto = venta.producto_id
            cantidad_vendida = venta.cantidad

            # Restar la cantidad vendida del producto
            producto.write({
                'cantidad': producto.cantidad - cantidad_vendida
            })

    total = fields.Float(string="Total a Cobrar", compute='_compute_total', store=True)
    @api.depends('producto_id', 'cantidad')
    def _compute_total(self):
        for venta in self:
            if venta.producto_id and venta.cantidad:
                venta.total = venta.producto_id.precio * venta.cantidad
            else:
                venta.total = 0.0

    fecha = fields.Datetime(string="Fecha", default=fields.Datetime.now)




class EntregaMercancia(models.Model):
    _name = 'mi_modulo.entrega_mercancia'

    productos_recibidos = fields.Many2many('mi_modulo.producto', string="Productos Recibidos")
    proveedor_id = fields.Many2one('mi_modulo.proveedor', string="Proveedor")
    fecha_entrega = fields.Datetime(string="Fecha", default=fields.Datetime.now)




class ControlVentasDiarias(models.Model):
    _name = 'mi_modulo.control_ventas_diarias'

    operador_id = fields.Many2one('mi_modulo.operador', string="Operador")
    productos_vendidos = fields.Many2many('mi_modulo.producto', string="Productos Vendidos")
    efectivo_total = fields.Float(string="Efectivo Total")
    fecha = fields.Date(string="Fecha")




class HorarioOperador(models.Model):
    _name = 'mi_modulo.horario_operador'

    nombre = fields.Char(string="Nombre")
    horas_trabajadas = fields.Float(string="Horas Trabajadas")
    dias_trabajados = fields.Integer(string="Días Trabajados")
