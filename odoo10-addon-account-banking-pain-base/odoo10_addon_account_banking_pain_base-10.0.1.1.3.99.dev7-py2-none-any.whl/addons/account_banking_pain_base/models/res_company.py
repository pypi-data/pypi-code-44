# -*- coding: utf-8 -*-
# © 2013-2016 Akretion - Alexis de Lattre <alexis.delattre@akretion.com>
# © 2013 Noviat (http://www.noviat.com) - Luc de Meyer
# © 2014 Serv. Tecnol. Avanzados - Pedro M. Baeza
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields, api
import logging

logger = logging.getLogger(__name__)


class ResCompany(models.Model):
    _inherit = 'res.company'

    initiating_party_issuer = fields.Char(
        string='Initiating Party Issuer', size=35,
        help="This will be used as the 'Initiating Party Issuer' in the "
        "PAIN files generated by Odoo.")
    initiating_party_identifier = fields.Char(
        string='Initiating Party Identifier', size=35,
        help="This will be used as the 'Initiating Party Identifier' in "
        "the PAIN files generated by Odoo.")
    initiating_party_scheme = fields.Char(
        string='Initiating Party Scheme', size=35,
        help="This will be used as the 'Initiating Party Scheme Name' in "
        "the PAIN files generated by Odoo.")

    @api.one
    def _default_initiating_party(self):
        '''This method is called from post_install.py'''
        party_issuer_per_country = {
            'BE': 'KBO-BCE',  # KBO-BCE = the registry of companies in Belgium
        }
        logger.debug(
            'Calling _default_initiating_party on company %s', self.name)
        country_code = self.country_id.code
        if not self.initiating_party_issuer:
            if country_code and country_code in party_issuer_per_country:
                self.write({
                    'initiating_party_issuer':
                    party_issuer_per_country[country_code]})
                logger.info(
                    'Updated initiating_party_issuer on company %s',
                    self.name)
        party_identifier = False
        if not self.initiating_party_identifier:
            if self.vat and country_code:
                if country_code == 'BE':
                    party_identifier = self.vat[2:].replace(' ', '')
            if party_identifier:
                self.write({
                    'initiating_party_identifier': party_identifier})
                logger.info(
                    'Updated initiating_party_identifier on company %s',
                    self.name)
