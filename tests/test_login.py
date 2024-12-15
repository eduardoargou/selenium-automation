from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.login_page import LoginPage
from pages.invoice_list_page import InvoiceListPage
from utils.assertions import assert_element_contains_text
import pytest


@pytest.mark.usefixtures('setup')
class TestLogin:

  username = 'demouser'
  password = 'abc123'
  failing_username = 'Demouser'
  failing_password = 'abc123'
  error_text = 'Wrong username or password'
  invoice_list_title_text = 'Invoice List'

  def test_successful_login(self):
    # Attempt login
    login_page = LoginPage(self.driver)
    login_page.enter_username(self.username)
    login_page.enter_password(self.password)
    login_page.click_login_button()
    # Validate invoice page
    invoice_list_page = InvoiceListPage(self.driver)
    invoice_list_title = invoice_list_page.get_invoice_list_title()
    assert_element_contains_text(invoice_list_title, self.invoice_list_title_text)

  def test_failed_login(self): 
    # Attempt login
    login_page = LoginPage(self.driver)
    login_page.enter_username(self.failing_username)
    login_page.enter_password(self.failing_password)
    login_page.click_login_button()
    # Validate error alert
    error_alert = login_page.get_error_alert()
    assert_element_contains_text(error_alert, self.error_text)
