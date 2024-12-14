from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import pytest

@pytest.fixture(scope='function')
def setup(request):
  url = 'https://automation-sandbox-python-mpywqjbdza-uc.a.run.app/'
  chrome_service = Service(ChromeDriverManager().install())
  driver = webdriver.Chrome(service=chrome_service)  
  driver.get(url)
  driver.maximize_window()
  request.cls.driver = driver
  yield
  driver.quit()
