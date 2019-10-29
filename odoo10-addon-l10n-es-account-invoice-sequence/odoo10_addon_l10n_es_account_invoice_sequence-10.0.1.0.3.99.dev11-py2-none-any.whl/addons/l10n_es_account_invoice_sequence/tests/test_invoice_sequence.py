# -*- coding: utf-8 -*-
# Copyright 2016 Pedro M. Baeza
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openerp.tests import common
from openerp import fields


@common.at_install(False)
@common.post_install(True)
class TestInvoiceSequence(common.HttpCase):
    def setUp(self):
        super(TestInvoiceSequence, self).setUp()
        self.sequence = self.env['ir.sequence'].create({
            'name': 'Test account move sequence',
            'padding': 3,
            'prefix': 'tAM',
        })
        self.invoice_sequence = self.env['ir.sequence'].create({
            'name': 'Test invoice sequence',
            'padding': 3,
            'prefix': 'tINV',
        })
        self.refund_sequence = self.env['ir.sequence'].create({
            'name': 'Test refund sequence',
            'padding': 3,
            'prefix': 'tREF',
        })
        self.journal = self.env['account.journal'].create({
            'name': 'Test Sales Journal',
            'code': 'tVEN',
            'type': 'sale',
            'sequence_id': self.sequence.id,
            'update_posted': True,
            'invoice_sequence_id': self.invoice_sequence.id,
            'refund_inv_sequence_id': self.refund_sequence.id,
        })
        self.account_type = self.env['account.account.type'].create({
            'name': 'Test',
            'type': 'receivable',
        })
        self.account = self.env['account.account'].create({
            'name': 'Test account',
            'code': 'TEST',
            'user_type_id': self.account_type.id,
            'reconcile': True,
        })
        self.account_income = self.env['account.account'].create({
            'name': 'Test income account',
            'code': 'INCOME',
            'user_type_id': self.env['account.account.type'].create(
                {'name': 'Test income'}).id,
        })

    def test_move_sequence(self):
        move = self.env['account.move'].create({
            'date': fields.Date.today(),
            'journal_id': self.journal.id,
            'name': '/',
            'ref': 'l10n_es_account_invoice_sequence',
            'state': 'draft',
            'line_ids': [(0, 0, {
                'account_id': self.account.id,
                'credit': 1000,
                'debit': 0,
                'name': 'Test',
                'ref': 'l10n_es_account_invoice_sequence',
            }), (0, 0, {
                'account_id': self.account.id,
                'credit': 0,
                'debit': 1000,
                'name': 'Test',
                'ref': 'l10n_es_account_invoice_sequence',
            })]})
        move.post()
        self.assertEqual(move.name[:3], 'tAM')

    def test_invoice_sequence(self):
        invoice = self.env['account.invoice'].create({
            'journal_id': self.journal.id,
            'account_id': self.account.id,
            'company_id': self.env.user.company_id.id,
            'currency_id': self.env.user.company_id.currency_id.id,
            'partner_id': self.env['res.partner'].create({'name': 'Test'}).id,
            'invoice_line_ids': [(0, 0, {
                'account_id': self.account_income.id,
                'name': 'Test line',
                'price_unit': 50,
                'quantity': 10,
            })]
        })
        invoice.action_invoice_open()
        self.assertEqual(invoice.number[:4], 'tINV')
        self.assertEqual(invoice.move_id.name[:3], 'tAM')
        self.assertEqual(invoice.move_id.ref[:4], 'tINV')
        invoice2 = invoice.copy()
        self.assertNotEqual(invoice.number, invoice2.number)
        # Cancel invoice and try to unlink
        invoice.action_invoice_cancel()
        invoice.unlink()  # This shouldn't raise error
        self.assertFalse(invoice.exists())

    def test_refund_sequence(self):
        invoice = self.env['account.invoice'].create({
            'journal_id': self.journal.id,
            'account_id': self.account.id,
            'type': 'out_refund',
            'company_id': self.env.user.company_id.id,
            'currency_id': self.env.user.company_id.currency_id.id,
            'partner_id': self.env['res.partner'].create({'name': 'Test'}).id,
            'invoice_line_ids': [(0, 0, {
                'account_id': self.account.id,
                'name': 'Test line',
                'price_unit': 50,
                'quantity': 10,
            })]
        })
        invoice.action_invoice_open()
        self.assertEqual(invoice.number[:4], 'tREF')
        self.assertEqual(invoice.move_id.name[:3], 'tAM')
        self.assertEqual(invoice.move_id.ref[:4], 'tREF')
