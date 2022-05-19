from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class extras(models.Model):
    # information propre a model's
    _name = "extras"
    _description = "this models is to refer to the services provides by the doc"
    # Fields
    codeExtras = fields.Char(string="Code Extras", required=True, readonly=True, index=True,
                             help="this is the fields that make each record unique")
    libelle = fields.Char(string="Libelle", required=True)
    prix =fields.Float(string="Prix")
    rdvs = fields.Many2many(comodel_name="gstrdv.rdvs", ondelete="set null", required=True, string="RDV")

    @api.model
    def create(self, vals):
        if vals.get('codeExtras', _('New')) == _('New'):
            vals['codeExtras'] = self.env['ir.sequence'].next_by_code('extras.sequence') or _('New')
        result = super(extras, self).create(vals)
        return result
