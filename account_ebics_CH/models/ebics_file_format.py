# Copyright 2020 Compassion.
# License LGPL-3 or later (http://www.gnu.org/licenses/lpgl).

from odoo import  models, fields


class EbicsFileFormat(models.Model):
    _inherit = 'ebics.file.format'

    display_name = fields.Char(
        compute='_display_name')

    def _supported_download_order_types(self):
        res = super()._supported_download_order_types()
        res.append("ZZT")
        res.append("ZZQ")
        return res
    
    def _display_name(self):
        self.display_name = self.name + " (" + self.order_type+")"
