from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

  def __init__(self, driver):
    self.driver = driver

  def wait_until_element_is_clickable(self, locator_type, locator):
    wait = WebDriverWait(self.driver, 5)
    return wait.until(EC.element_to_be_clickable((locator_type, locator)))
  
  def wait_until_element_is_present(self, locator_type, locator):
    wait = WebDriverWait(self.driver, 5)
    return wait.until(EC.presence_of_element_located((locator_type, locator)))

  def handle_new_tab(self, current_window_handle):
    wait = WebDriverWait(self.driver, 5)
    wait.until(EC.number_of_windows_to_be(2))
    for window_handle in self.driver.window_handles:
      if window_handle != current_window_handle:
        self.driver.switch_to.window(window_handle)
        break
