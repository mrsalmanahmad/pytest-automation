import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def browser():
  # use this in-case your env path of chromedriver is not setup  
  driver = webdriver.Chrome('C:/Users/Sulman/chromedriver.exe') 
  # use this if your env path of chromedriver is already setup
 # driver = Chrome()
  driver.implicitly_wait(10)
  yield driver
  driver.quit()
  