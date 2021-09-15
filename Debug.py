import win32com.client
from selenium.webdriver import ActionChains
from test_Framework.test_scripts.conftest import ChromeBrowserSetup

URL = "https://www.ndtv.com/business"
driver = ChromeBrowserSetup(URL)

print(driver.find_element_by_xpath("//*[@class='widcont_topstories']//div[@class='headline']//a").get_attribute("href"))
Links=driver.find_elements_by_xpath("//*[@class='widcont_topstories']//*[@class='bud_otherstories1']//li//p/a")
for i in Links:
    print(i.get_attribute("href"))

assert driver.find_element_by_xpath("//*[@alt='News']").get_attribute("title")=="News"
Actions=ActionChains(driver)
Actions.move_to_element(driver.find_element_by_xpath("//*[@alt='News']")).perform()
Actions.context_click().perform()
wsh=  win32com.client.Dispatch("WScript.Shell") #pip install pywin32 and import win32com.client
wsh.SendKeys("{DOWN}")
wsh.SendKeys("{DOWN}")
wsh.SendKeys("{ENTER}")
Handles=driver.window_handles
print(Handles)
driver.switch_to_window(Handles[1])
Collect=driver.find_elements_by_xpath("//*[@class='news_Itm']//*[@class='newsHdng']/a")
for i in Collect:
    print(i.get_attribute("href"))
    if i==3:
        break

