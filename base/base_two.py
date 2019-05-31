from selenium.webdriver.support.wait import WebDriverWait


class BaseTwo():
    def __init__(self,driver):
        self.driver = driver


    def find(self,loc):
        return  WebDriverWait(self.driver,10,1).until(lambda x:x.find_element(*loc))

    def click(self,loc):
        self.find(loc).click()

    def input(self,loc,value):
        self.find(loc).clear()
        self.find(loc).send_keys(value)



