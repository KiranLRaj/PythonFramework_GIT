import pytest
from selenium.webdriver import ActionChains

from test_Framework.PageObjects.HomePage import HomePage
from test_Framework.test_scripts.conftest import ChromeBrowserSetup, GetFullScreenShotHeadless


class Test_Questions:

    def test_Ques2_1(self):
        driver=ChromeBrowserSetup()
        driver.get("https://www.rediff.com/")
        HomePage(driver).newslink().click()
        # driver.find_element_by_xpath("//*[text()='NEWS']").click()
        GetFullScreenShotHeadless(driver.current_url,"SS1")
        Links=HomePage(driver).submenulinks()
        for i in Links:
            print(i.get_attribute("href"))
        assert driver.find_element_by_xpath("//*[text()='BUSINESS']").get_attribute("title") == "Business headlines"
        Actions=ActionChains(driver)
        Actions.move_to_element(driver.find_element_by_xpath("//*[text()='BUSINESS']"))
        # driver.save_screenshot("C:\\Users\Raj\PycharmProjects\PythonFramework\\test_Framework\Screenshots\\test_Ques2_ToolTip")


