from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LoginPage:

  username_input = '//input[@name="username"]'
  password_input = '//input[@name="password"]'
  login_button = '//button[@id="btnLogin"]'

  def __init__(self, driver):
    self.driver = driver

  def enter_username(self, username):
    wait = WebDriverWait(self.driver, 5)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, self.username_input)))
    element.send_keys(username)

  def enter_password(self, password):
    wait = WebDriverWait(self.driver, 5)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, self.password_input)))
    element.send_keys(password)

  def click_login_button(self):
    wait = WebDriverWait(self.driver, 5)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, self.login_button)))
    element.click()
