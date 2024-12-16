import pytest
from pages.login_page import LoginPage
from pages.invoice_list_page import InvoiceListPage
from pages.invoice_details_page import InvoiceDetailsPage
from utils.assertions import assert_invoice_details_match
import softest


@pytest.mark.usefixtures('setup')
class TestInvoices(softest.TestCase):

  details = {
    'hotel_name': 'Rendezvous Hotel',
    'invoice_date': '14/01/2018',
    'due_date': '15/01/2018',
    'invoice_number': '110',
    'booking_code': '0875',
    'customer_details': 'JOHNY SMITH\nR2, AVENUE DU MAROC\n123456',
    'room': 'Superior Double',
    'check_in': '14/01/2018',
    'check_out': '15/01/2018',
    'total_stay_count': '1',
    'total_stay_amount': '$150',
    'deposit_now': 'USD $20.90',
    'tax_and_vat': 'USD $19.00',
    'total_amount': 'USD $209.00'
  }

  def test_invoice_details(self):
    # Login
    login_page = LoginPage(self.driver)
    login_page.attempt_login('demouser', 'abc123')
    # Click first invoice details
    invoice_list_page = InvoiceListPage(self.driver)
    invoice_list_page.click_invoice_details(0)
    # Validate details data
    page = InvoiceDetailsPage(self.driver)
    assert_invoice_details_match(self, page, self.details)
