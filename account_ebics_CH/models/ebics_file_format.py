# Copyright 2020 Compassion.
# License LGPL-3 or later (http://www.gnu.org/licenses/lpgl).

from odoo import api, models, _
from odoo.exceptions import UserError


class EbicsFileFormat(models.Model):
    _inherit = 'ebics.file.format'

    def _supported_download_order_types(self):
        res = super()
        res.append("ZZT")
        res.append("ZZQ")
        return res
