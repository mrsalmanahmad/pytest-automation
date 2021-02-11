import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from browser_setup import browser

def test_basic_duckduckgo_search(browser):
  URL = 'https://pocketfactory-qa.ssidecisions.com/PocketFactory'
  ID = 'ssi'
  PASS = 'ABC123ssi'

  browser.get(URL)
  
  search_input = browser.find_element_by_id('userName')
  search_input.send_keys(ID)
  
  seach_password = browser.find_element_by_id('password')
  seach_password.send_keys(PASS + Keys.RETURN)

 # browser.find_element_by_name('Button1').click()
  Blow_Molder = browser.find_element_by_id('398').is_displayed()
  assert Blow_Molder == True, 'Blow_Molder is Present on the Screen'
  Labler = browser.find_element_by_id('401').is_displayed() 
  assert Labler == True
  print('Labler is Present on the Screen')
  Cip_Mixer = browser.find_element_by_id('440').is_displayed() 
  assert Cip_Mixer == True
  print('Cip_Mixer is Present on the Screen')
  Cip_Filler = browser.find_element_by_id('399').is_displayed() 
  assert Cip_Filler == True
  print('Cip_Filler is Present on the Screen')
  Filler = browser.find_element_by_id('400').is_displayed() 
  assert Filler == True
  print('Filler is Present on the Screen')
  Packer_1   = browser.find_element_by_id('402').is_displayed()
  assert Packer_1 == True
  print('Packer 1 is Present on the Screen')
  Packer_2 = browser.find_element_by_id('403').is_displayed() 
  assert Packer_2 == True
  print('Packer 02 is Present on the Screen')
  Pallertizer = browser.find_element_by_id('404').is_displayed()    
  assert Pallertizer == True
  print('Pallertizer is Present on the Screen')  

 # browser.find_element_by_id('401').click()
#   link_divs = browser.find_elements_by_css_selector('#links > div')
#   assert len(link_divs) > 0
  
#   xpath = f"//div[@id='links']//*[contains(text(), '{PHRASE}')]"
#   results = browser.find_elements_by_xpath(xpath)
#   assert len(results) > 0
  
#   search_input = browser.find_element_by_id('search_form_input')
#   assert search_input.get_attribute('value') == PHRASE 
  
