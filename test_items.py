import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By

def test_basket_button_present(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    basket_button = len(browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket"))
    assert basket_button > 0, "The button is missing"
        
    
    
    
