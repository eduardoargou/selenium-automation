from .base_page import BasePage
from selenium.webdriver.common.by import By


class InvoiceDetailsPage(BasePage):

  hotel_name_header = '//h4[@class="mt-5"]'
  invoice_date_item = '(//div/ul/li)[1]'
  due_date_item = '(//div/ul/li)[2]'
  invoice_number_header = '//h6[@class="mt-2"]'
  booking_code = '(//tbody/tr/td)[2]'
  customer_details = '//section/div/div'
  room = '(//tbody/tr/td)[4]'
  check_in = '(//tbody/tr/td)[10]'
  check_out = '(//tbody/tr/td)[12]'
  total_stay_count = '(//tbody/tr/td)[6]'
  total_stay_amount = '(//tbody/tr/td)[8]'
  deposit_now = '(//tbody/tr/td)[13]'
  tax_and_vat = '(//tbody/tr/td)[14]'
  total_amount = '(//tbody/tr/td)[15]'

  def __init__(self, driver):
    super().__init__(driver)

  def get_hotel_name(self):
    element = self.wait_until_element_is_present(By.XPATH, self.hotel_name_header)
    return element.text

  def get_invoice_date(self):
    element = self.wait_until_element_is_present(By.XPATH, self.invoice_date_item)
    return element.text.split()[-1].strip()

  def get_due_date(self):
    element = self.wait_until_element_is_present(By.XPATH, self.due_date_item)
    return element.text.split()[-1].strip()

  def get_invoice_number(self):
    element = self.wait_until_element_is_present(By.XPATH, self.invoice_number_header)
    return element.text.split()[1].strip('#')

  def get_booking_code(self):
    element = self.wait_until_element_is_present(By.XPATH, self.booking_code)
    return element.text

  def get_customer_details(self):
    element = self.wait_until_element_is_present(By.XPATH, self.customer_details)
    return element.text.strip()

  def get_room(self):
    element = self.wait_until_element_is_present(By.XPATH, self.room)
    return element.text

  def get_check_in(self):
    element = self.wait_until_element_is_present(By.XPATH, self.check_in)
    return element.text

  def get_check_out(self):
    element = self.wait_until_element_is_present(By.XPATH, self.check_out)
    return element.text

  def get_total_stay_count(self):
    element = self.wait_until_element_is_present(By.XPATH, self.total_stay_count)
    return element.text

  def get_total_stay_amount(self):
    element = self.wait_until_element_is_present(By.XPATH, self.total_stay_amount)
    return element.text

  def get_deposit_now(self):
    element = self.wait_until_element_is_present(By.XPATH, self.deposit_now)
    return element.text

  def get_tax_and_vat(self):
    element = self.wait_until_element_is_present(By.XPATH, self.tax_and_vat)
    return element.text

  def get_total_amount(self):
    element = self.wait_until_element_is_present(By.XPATH, self.total_amount)
    return element.text
