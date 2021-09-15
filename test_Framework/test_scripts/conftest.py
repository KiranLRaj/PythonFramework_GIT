import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def ChromeBrowserSetup():
    options=Options()
    options.add_argument("--disable-notifications")
    driver=webdriver.Chrome(executable_path="C:\\Selenium\chromedriver.exe",options=options)
    driver.maximize_window()
    return driver




def GetFullScreenShotHeadless(url,AppendValue):
    options=Options()
    options.add_argument("Headless")
    driver = webdriver.Chrome(executable_path="C:\\Selenium\chromedriver.exe", options=options)
    driver.get(url)
    TestName = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
    Path = "C:\\Users\\Raj\PycharmProjects\\PythonFramework\\test_Framework\Screenshots\\" + TestName + "_" + AppendValue + ".PNG"
    required_width = driver.execute_script('return document.body.parentNode.scrollWidth')
    required_height = driver.execute_script('return document.body.parentNode.scrollHeight')
    driver.set_window_size(required_width, required_height)
    driver.save_screenshot(Path)
    driver.quit()