from pages.invoice_details_page import InvoiceDetailsPage


def assert_element_contains_text(element, text):
  assert text in element.text

def assert_invoice_details_match(test, page, details):
  soft_assert_eq(test, page.get_hotel_name(), details['hotel_name'])
  soft_assert_eq(test, page.get_invoice_date(), details['invoice_date'])
  soft_assert_eq(test, page.get_due_date(), details['due_date'])
  soft_assert_eq(test, page.get_invoice_number(), details['invoice_number'])
  soft_assert_eq(test, page.get_booking_code(), details['booking_code'])
  soft_assert_eq(test, page.get_customer_details(), details['customer_details'])
  soft_assert_eq(test, page.get_room(), details['room'])
  soft_assert_eq(test, page.get_check_in(), details['check_in'])
  soft_assert_eq(test, page.get_check_out(), details['check_out'])
  soft_assert_eq(test, page.get_total_stay_count(), details['total_stay_count'])
  soft_assert_eq(test, page.get_total_stay_amount(), details['total_stay_amount'])
  soft_assert_eq(test, page.get_deposit_now(), details['deposit_now'])
  soft_assert_eq(test, page.get_tax_and_vat(), details['tax_and_vat'])
  soft_assert_eq(test, page.get_total_amount(), details['total_amount'])
  test.assert_all()

def soft_assert_eq(test, actual, expected):
  test.soft_assert(test.assertEqual, actual, expected)
