import allure
from selenium.webdriver.common.by import By

from base.base_two import  BaseTwo

class PageOne(BaseTwo):
    new1 = By.XPATH,"//*[@content-desc='添加新联系人']"

    @allure.step(title="点击添加")
    def newconcat(self):
        self.click(self.new1)

