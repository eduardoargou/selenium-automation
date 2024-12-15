from .base_page import BasePage
from selenium.webdriver.common.by import By


class InvoiceListPage(BasePage):

  invoice_list_title = '//*[text()[contains(.,"Invoice List")]]'

  def __init__(self, driver):
    super().__init__(driver)

  def get_invoice_list_title(self):
    return self.wait_until_element_is_present(By.XPATH, self.invoice_list_title)
