from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self,driver):
        self.driver=driver


    # All Objects

    NewsLink=(By.XPATH,"//*[text()='NEWS']")
    SubMenuLinks=(By.XPATH,"//*[contains(@class,'subnavbar')]/ul/li/a")

    # Methods to return objects

    def newslink(self):
        return self.driver.find_element(*HomePage.NewsLink)

    def submenulinks(self):
        return self.driver.find_elements(*HomePage.SubMenuLinks)