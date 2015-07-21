# -*- coding: utf-8 -*- 
# copyrigth (c) 2015 Javier Campana <jcampana@cyg.ec>
__author__ = 'Javier'

from openerp.osv import osv, fields

class calculadora(osv.osv):
    """
    Clase principal de la calculadora
    """
    _name = "cyg.calculadora"
    _description = "Clase que contiene la calculadora"

    _columns = {
        'name': fields.char('Nombre', size=64),
        'a': fields.float('A'),
        'b': fields.float('B'),
        'total': fields.float('Total'),
    }