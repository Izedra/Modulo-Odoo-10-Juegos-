from odoo import models, fields, api

class Consolas(models.Model):
    _name = 'juegos.consolas'
    consola = fields.Char('Consola', required=True)
    plataforma = fields.Many2one('juegos.plataforma', 'Plataformas')

    def name_get(self):
        res=[]
        for record in self:
            name = record.consola
            res.append((record.id, name))
        return res
