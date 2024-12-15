from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.login_page import LoginPage
from pages.invoice_list_page import InvoiceListPage
from utils.assertions import assert_element_contains_text
import pytest


@pytest.mark.usefixtures('setup')
class TestLogin:

  invoice_list_title_text = 'Invoice List'
  error_text = 'Wrong username or password'
  working_credentials = [('demouser', 'abc123')]
  failing_credentials = [
    ('Demouser', 'abc123'),
    ('demouser_', 'xyz'),
    ('demouser', 'nananana'),
    ('demouser', 'abc123')
  ]

  @pytest.mark.parametrize("username, password", working_credentials)
  def test_successful_login(self, username, password):
    # Attempt login
    login_page = LoginPage(self.driver)
    login_page.attempt_login(username, password)
    # Validate invoice page
    invoice_list_page = InvoiceListPage(self.driver)
    invoice_list_title = invoice_list_page.get_invoice_list_title()
    assert_element_contains_text(invoice_list_title, self.invoice_list_title_text)

  @pytest.mark.parametrize("username, password", failing_credentials)
  def test_failed_login(self, username, password): 
    # Attempt login
    login_page = LoginPage(self.driver)
    login_page.attempt_login(username, password)
    # Validate error alert
    error_alert = login_page.get_error_alert()
    assert_element_contains_text(error_alert, self.error_text)
