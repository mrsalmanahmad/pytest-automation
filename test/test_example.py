# Import the 'modules' that are required for execution for Selenium test automation
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from time import sleep
import sys
 
#Fixture for Firefox
@pytest.fixture(scope="class")
def driver_init(request):
    ff_driver = webdriver.Firefox()
    request.cls.driver = ff_driver
    yield
    ff_driver.close()
 
#Fixture for Chrome
@pytest.fixture(scope="class")
def chrome_driver_init(request):
    chrome_driver = webdriver.Chrome()
    request.cls.driver = chrome_driver
    yield
    chrome_driver.close()
 
@pytest.mark.usefixtures("chrome_driver_init")
class BasicTest:
    pass
class Test_URL(BasicTest):
    def test_open_url(self):
        self.driver.get('https://www.google.com/')
        self.driver.maximize_window()
        title = "Google"
        assert title == self.driver.title
 
        search_text = "LambdaTest"
        search_box = self.driver.find_element_by_xpath("//input[@name='q']")
        search_box.send_keys(search_text)
 
        time.sleep(5)
 
        # Option 1 - To Submit the search
        # search_box.submit()
 
        # Option 2 - To Submit the search
        search_box.send_keys(Keys.ARROW_DOWN)
        search_box.send_keys(Keys.ARROW_UP)
        time.sleep(2)
        search_box.send_keys(Keys.RETURN)
 
        time.sleep(5)
 
        # Click on the LambdaTest HomePage Link
        title = "Most Powerful Cross Browser Testing Tool Online | LambdaTest"
        lt_link = self.driver.find_element_by_xpath("//h3[.='LambdaTest: Most Powerful Cross Browser Testing Tool Online']")
        lt_link.click()
 
        time.sleep(10)
        assert title == self.driver.title   
        time.sleep(2)
 
@pytest.mark.usefixtures("chrome_driver_init")
class Basic_Chrome_Test: 
    pass
class Test_URL_Chrome(Basic_Chrome_Test):
    def test_open_url(self):
        self.driver.get('https://lambdatest.github.io/sample-todo-app/')
        self.driver.maximize_window()
 
        self.driver.find_element_by_name("li1").click()
        self.driver.find_element_by_name("li2").click()
 
        title = "Sample page - lambdatest.com"
        assert title ==  self.driver.title
 
        sample_text = "Happy Testing at LambdaTest"
        email_text_field =  self.driver.find_element_by_id("sampletodotext")
        email_text_field.send_keys(sample_text)
        time.sleep(5)
 
        self.driver.find_element_by_id("addbutton").click()
        time.sleep(5)
 
        output_str =  self.driver.find_element_by_name("li6").text
        sys.stderr.write(output_str)
 
        time.sleep(2) 