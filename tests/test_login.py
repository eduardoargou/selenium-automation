from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.login_page import LoginPage

class TestLogin:

  username = 'demouser'
  password = 'abc123'

  def test_successful_login(self):
    # Visit page
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    url = 'https://automation-sandbox-python-mpywqjbdza-uc.a.run.app/'
    driver.get(url)
    driver.maximize_window()
    # Attempt login
    login_page = LoginPage(driver)
    login_page.enter_username(self.username)
    login_page.enter_password(self.password)
    login_page.click_login_button()
    # Validate invoice page
    wait = WebDriverWait(driver, 5)
    invoice_list_title = wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//*[text()[contains(.,"Invoice List")]]')))
    assert invoice_list_title[0].text == 'Invoice List'
