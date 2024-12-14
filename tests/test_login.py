from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.login_page import LoginPage
import pytest


@pytest.mark.usefixtures('setup')
class TestLogin:

  username = 'demouser'
  password = 'abc123'

  failing_username = 'Demouser'
  failing_password = 'abc123'

  def test_successful_login(self):
    # Attempt login
    login_page = LoginPage(self.driver)
    login_page.enter_username(self.username)
    login_page.enter_password(self.password)
    login_page.click_login_button()
    # Validate invoice page
    wait = WebDriverWait(self.driver, 5)
    invoice_list_title = wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//*[text()[contains(.,"Invoice List")]]')))
    assert invoice_list_title[0].text == 'Invoice List'

  def test_failed_login(self):
    # Attempt login
    login_page = LoginPage(self.driver)
    login_page.enter_username(self.failing_username)
    login_page.enter_password(self.failing_password)
    login_page.click_login_button()
    # Validate error alert
    error_alert = login_page.get_error_alert()
    assert 'Wrong username or password' in error_alert.text
