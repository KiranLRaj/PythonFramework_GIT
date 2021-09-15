# import time
#
# import pytest
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.keys import Keys
# from Utilities.JavaScriptOperations import JSOperations
# from Utilities.Utilities import Utilities
# from test_Framework.conftest import ChromeBrowserSetup, GetFullScreenShotHeadless
#
#
# class Test_Questions:
#
#     @pytest.mark.skip
#     @pytest.mark.order(1)
#     def test_Ques1(self):
#         URL = "http://www.pepperfry.com/"
#         driver = ChromeBrowserSetup(URL)
#         print(driver.title)
#         # Crete objects of all the classes you use
#         JS = JSOperations(driver)
#         Utility = Utilities(driver)
#         # -----------------------------------
#         FilePath = "C:\\Users\Raj\Desktop\Data.xlsx"
#         SearchValues = Utility.ExcelDataOneColumn(FilePath, "Sheet1")
#         for i in SearchValues:
#             driver.find_element_by_xpath("//*[@id='search']").click()
#             driver.find_element_by_xpath("//*[@id='search']").send_keys(i + Keys.ENTER)
#             NoResults = "// *[contains(text(), 'No results found for ')]"
#             if Utility.CheckElementExists(NoResults) == False:
#                 driver.find_element_by_xpath("//*[contains(@class,'selct-drp-dwn')]").click()
#                 Element = driver.find_element_by_xpath("//*[contains(text(),'Price Low to High')]")
#                 JS.JSClick(Element)
#                 driver.find_element_by_xpath("//*[@class='head-pepperfry-logo']").click()
#
#     @pytest.mark.skip
#     @pytest.mark.order(2)
#     def test_Ques2(self):
#         URL = "https://www.wikipedia.org/"
#         driver = ChromeBrowserSetup(URL)
#         JS = JSOperations(driver)
#         print("Number of English Articles are : " + driver.find_element_by_xpath(
#             "//*[@id='js-link-box-en']/small/bdi").text)
#         JS.JSClick(driver.find_element_by_xpath("//*[@id='js-link-box-en']/small/bdi"))
#         driver.find_element_by_xpath("//*[@id='searchInput']").click()
#         driver.find_element_by_xpath("//*[@id='searchInput']").send_keys("Anna University" + Keys.ENTER)
#         driver.find_element_by_xpath("//*[@title='Anna University']").click()
#         Motto = driver.find_element_by_xpath(
#             "//*[@class='infobox-data' and preceding-sibling::*[@class='infobox-label' and child::*[contains(text(),'Motto in')]]]").text
#         assert Motto.find("Knowledge") >= 0
#         Names = driver.find_elements_by_xpath(
#             "//ul[preceding-sibling::*[@class='box-Alumni plainlinks metadata ambox ambox-style']]/li/a")
#         for i in range(0, len(Names), 2):
#             if Names[i] == "Ravichandran Ashwin":
#                 print("Name present in Notable People section")
#                 break
#
#     def test_Ques3(self):
#
#         URL = "https://mu.ac.in/"
#         driver = ChromeBrowserSetup(URL)
#         JS = JSOperations(driver)
#         Actions = ActionChains(driver)
#         AcademicsElement = \
#         driver.find_elements_by_xpath("//li[@id='menu-item-2100' and child::*[contains(text(),'ACADEMICS')]]")[0]
#         Actions.move_to_element(AcademicsElement)
#         Actions.move_to_element(driver.find_elements_by_xpath("//a[contains(text(),'FACULTY')]")[0])
#         Actions.move_to_element(
#             driver.find_elements_by_xpath("//a[contains(text(),'SCIENCE & TECHNOLOGY')]")[0]).click().perform()
#         JS.JSClick(driver.find_element_by_xpath("//a[contains(text(),'DEPARTMENT OF INFORMATION TECHNOLOGY')]"))
#         time.sleep(3)
#         Handles = driver.window_handles
#         driver.switch_to.window(Handles[1])
#         print(driver.find_element_by_xpath("//p/b[contains(text(),'Vision')]").get_attribute("innerHTML"))
#         for i in driver.find_elements_by_xpath("//div[@class='fs-text-desc']/p"):
#             print(i.get_attribute("innerHTML"))
#         assert str(driver.find_elements_by_xpath("//div[@class='fs-text-desc']/p")[1].get_attribute("innerHTML")).find(
#             "022-26500208") >= 0
#         assert str(driver.find_elements_by_xpath("//div[@class='fs-text-desc']/p")[1].get_attribute("innerHTML")).find(
#             "uditoffice@gmail.com") >= 0
#         GetFullScreenShotHeadless(driver.current_url)
#
#
#
#
#
#
#
#
