from odoo import models, fields, api

class JuegosJuegos(models.Model):
    _name = 'juegos.juegos'
    codigo = fields.Integer('Codigo', required=True)
    desarrolladora = fields.Char('Desarrolladora', required=True)
    nombre = fields.Char('Nombre', required=True)
    plataforma = fields.Many2one('juegos.plataformas', 'Plataforma')
    consola = fields.Many2one('juegos.consolas', 'Consola')

    @api.one
    def limpiar(self):
        self.desarrolladora = ""
	self.nombre = ""
        return True

    @api.multi
    def limpia_todo(self):
        done_recs = self.search([('desarrolladora', '=', '')])
        done_recs.write({'desarrolladora': ''})
        return True
