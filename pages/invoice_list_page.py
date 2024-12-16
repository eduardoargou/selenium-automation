from .base_page import BasePage
from selenium.webdriver.common.by import By


class InvoiceListPage(BasePage):

  invoice_list_title = '//*[text()[contains(.,"Invoice List")]]'
  invoice_link = '//a[@href="/invoice/{0}"]'

  def __init__(self, driver):
    super().__init__(driver)

  def get_invoice_list_title(self):
    return self.wait_until_element_is_present(By.XPATH, self.invoice_list_title)

  def click_invoice_details(self, invoice_id):
    link = self.invoice_link.format(invoice_id)
    element = self.wait_until_element_is_clickable(By.XPATH, link)
    current_window_handle = self.driver.current_window_handle
    element.click()
    self.handle_new_tab(current_window_handle)
