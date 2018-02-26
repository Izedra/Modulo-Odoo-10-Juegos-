from odoo import models, fields

class Plataformas(models.Model):
    _name = 'juegos.plataformas'
    codigo = fields.Integer('Codigo', required=True)
    plataforma = fields.Char('Compania de la consola', required=True)

    def name_get(self):
        res=[]
        for record in self:
            name = record.plataforma
            res.append((record.id, name))
        return res

class Consolas(models.Model):
    _name = 'juegos.consolas'
    consola = fields.Char('Consola', required=True)
    plataforma = fields.Many2one('juegos.plataformas', 'Plataformas')

    def name_get(self):
        res=[]
        for record in self:
            name = record.consola
            res.append((record.id, name))
        return res
