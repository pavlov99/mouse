""" Test parser functionality."""
import datetime
import decimal
import unittest

from ..parser import etree, CheddargetterParser


class CheddargetterParserTest(unittest.TestCase):
    def setUp(self):
        with open("mouse/tests/xml/plans.xml") as f:
            self.xml_plans = f.read()
        with open("mouse/tests/xml/customers.xml") as f:
            self.xml_customers = f.read()
        with open("mouse/tests/xml/error.xml") as f:
            self.xml_error = f.read()

    def _check_obj_type(self, obj, type_=None, is_required=None):
        self.assertTrue(
            (not is_required and obj is None) or
            isinstance(obj, type_ or str)
        )

    def _check_plans(self, plans):
        for plan in plans:
            self._check_obj_type(plan.id)
            self._check_obj_type(plan.code)
            self._check_obj_type(plan.name)
            self._check_obj_type(plan.description)
            self._check_obj_type(plan.isActive, bool)
            self._check_obj_type(plan.isFree, bool)
            self._check_obj_type(plan.trialDays, int)
            self._check_obj_type(plan.billingFrequency)
            self._check_obj_type(plan.billingFrequencyPer)
            self._check_obj_type(plan.billingFrequencyUnit)
            self._check_obj_type(plan.billingFrequencyQuantity, int)
            self._check_obj_type(plan.setupChargeCode)
            self._check_obj_type(plan.setupChargeAmount, decimal.Decimal)
            self._check_obj_type(plan.recurringChargeCode)
            self._check_obj_type(plan.recurringChargeAmount, decimal.Decimal)
            print(plan.createdDatetime)
            self._check_obj_type(plan.createdDatetime, datetime.datetime)

            for item in plan.items:
                self._check_obj_type(item.id)
                self._check_obj_type(item.code)
                self._check_obj_type(item.name)
                self._check_obj_type(item.quantityIncluded, decimal.Decimal)
                self._check_obj_type(item.isPeriodic, bool)
                self._check_obj_type(item.overageAmount, decimal.Decimal)
                self._check_obj_type(item.createdDatetime, datetime.datetime)

    def test_parse_plans(self):
        """ Test fixture parse."""
        tag, plans = CheddargetterParser.parse(
            etree.fromstring(self.xml_plans))
        self._check_plans(plans)

    def test_parse_customers(self):
        tag, customers = CheddargetterParser.parse(
            etree.fromstring(self.xml_customers))
        for customer in customers:
            self._check_obj_type(customer.id)
            self._check_obj_type(customer.code)
            self._check_obj_type(customer.firstName)
            self._check_obj_type(customer.lastName)
            self._check_obj_type(customer.company)
            self._check_obj_type(customer.email)
            self._check_obj_type(customer.gatewayToken)
            self._check_obj_type(customer.isVatExempt, bool)
            self._check_obj_type(customer.vatNumber)
            self._check_obj_type(
                customer.firstContactDatetime, datetime.datetime)
            self._check_obj_type(customer.referer)
            self._check_obj_type(customer.refererHost)
            self._check_obj_type(customer.campaignSource)
            self._check_obj_type(customer.campaignMedium)
            self._check_obj_type(customer.campaignTerm)
            self._check_obj_type(customer.campaignContent)
            self._check_obj_type(customer.campaignName)
            self._check_obj_type(customer.createdDatetime, datetime.datetime)
            self._check_obj_type(customer.modifiedDatetime, datetime.datetime)

            for subscription in customer.subscriptions:
                self._check_plans(subscription.plans)
                self._check_obj_type(subscription.gatewayToken)
                self._check_obj_type(subscription.gatewayAccount.id)
                self._check_obj_type(subscription.gatewayAccount.gateway)
                self._check_obj_type(subscription.gatewayAccount.type)
                self._check_obj_type(subscription.ccFirstName)
                self._check_obj_type(subscription.ccLastName)
                self._check_obj_type(subscription.ccCompany)
                self._check_obj_type(subscription.ccCountry)
                self._check_obj_type(subscription.ccAddress)
                self._check_obj_type(subscription.ccCity)
                self._check_obj_type(subscription.ccState)
                self._check_obj_type(subscription.ccZip)
                self._check_obj_type(subscription.ccType)
                self._check_obj_type(subscription.ccLastFour)
                self._check_obj_type(
                    subscription.ccExpirationDate, datetime.date)
                self._check_obj_type(
                    subscription.canceledDatetime, datetime.datetime)
                self._check_obj_type(
                    subscription.createdDatetime, datetime.datetime)

                for item in getattr(subscription, "items", []):
                    self._check_obj_type(item.id)
                    self._check_obj_type(item.code)
                    self._check_obj_type(item.name)
                    self._check_obj_type(item.quantity, decimal.Decimal)
                    self._check_obj_type(
                        item.createdDatetime, datetime.datetime)
                    self._check_obj_type(
                        item.modifiedDatetime, datetime.datetime)

                for invoice in subscription.invoices:
                    self._check_obj_type(invoice.id)
                    self._check_obj_type(invoice.number)
                    self._check_obj_type(invoice.type)
                    self._check_obj_type(invoice.vatRate)
                    self._check_obj_type(
                        invoice.billingDatetime, datetime.datetime)
                    self._check_obj_type(invoice.paidTransactionId)
                    self._check_obj_type(
                        invoice.createdDatetime, datetime.datetime)

                    for charge in invoice.charges:
                        self._check_obj_type(charge.id)
                        self._check_obj_type(charge.code)
                        self._check_obj_type(charge.type)
                        self._check_obj_type(charge.quantity, decimal.Decimal)
                        self._check_obj_type(
                            charge.eachAmount, decimal.Decimal)
                        self._check_obj_type(charge.description)
                        self._check_obj_type(
                            charge.createdDatetime, datetime.datetime)

                    for transaction in getattr(invoice, "transactions", []):
                        # self._check_obj_type(invoice.)
                        pass

    def test_error_pass(self):
        tag, error = CheddargetterParser.parse(
            etree.fromstring(self.xml_error))
        self.assertEqual(error.id, "73542")
        self.assertEqual(error.code, 404)
        self.assertEqual(error.auxCode, None)
        self.assertEqual(error.message, "Customer not found")
        self.assertTrue(isinstance(error, Exception))
