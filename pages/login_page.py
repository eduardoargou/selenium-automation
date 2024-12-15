from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):

  username_input = '//input[@name="username"]'
  password_input = '//input[@name="password"]'
  login_button = '//button[@id="btnLogin"]'
  error_alert = '//div[@role="alert"]'

  def __init__(self, driver):
    super().__init__(driver)

  def enter_username(self, username):
    element = self.wait_until_element_is_clickable(By.XPATH, self.username_input)
    element.send_keys(username)

  def enter_password(self, password):
    element = self.wait_until_element_is_clickable(By.XPATH, self.password_input)
    element.send_keys(password)

  def click_login_button(self):
    element = self.wait_until_element_is_clickable(By.XPATH, self.login_button)
    element.click()

  def get_error_alert(self):
    return self.wait_until_element_is_present(By.XPATH, self.error_alert)
