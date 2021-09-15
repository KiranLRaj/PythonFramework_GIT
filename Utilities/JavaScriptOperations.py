import time

class JSOperations:

    def __init__(self,driver):
        self.driver=driver

    def JSClick(self,element):
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(2)

    def JSType(self,element,TypeValue):
        self.driver.execute_script("arguments[0].click();", element)
        self.driver.execute_script("",element)
        self.driver.execute_script("arguments[0].value=\'"+TypeValue+"\';",element)
        time.sleep(1)
