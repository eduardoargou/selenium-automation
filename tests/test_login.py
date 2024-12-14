from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestLogin:

  username = 'demouser'
  password = 'abc123'

  def test_successful_login(self):
    # Visit page
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    url = 'https://automation-sandbox-python-mpywqjbdza-uc.a.run.app/'
    driver.get(url)
    driver.maximize_window()
    # Enter username
    wait = WebDriverWait(driver, 5)
    username_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@name="username"]')))
    username_input.send_keys(self.username)
    # Enter password
    password_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@name="password"]')))
    password_input.send_keys(self.password)
    # Click button
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@id="btnLogin"]')))
    login_button.click()
    # Validate invoice page
    invoice_list_title = wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//*[text()[contains(.,"Invoice List")]]')))
    assert invoice_list_title[0].text == 'Invoice List'
