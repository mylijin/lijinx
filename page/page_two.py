import allure
from selenium.webdriver.common.by import By

from base.base_two import BaseTwo


class PageTwo(BaseTwo):
    new1 = By.XPATH, "//*[@text='姓名']"
    new2 = By.XPATH, "//*[@text='电话']"

    @allure.step(title="输入姓名")
    def name(self,value):
        self.input(self.new1,value)

    @allure.step(title="输入电话")
    def phone(self,value):
        self.input(self.new2,value)
        # self.driver.get_screenshot_as_file("img/xx.png")
        # with open("img/xx.png", "rb") as f:
        #     allure.attach('截图', f.read(), allure.attach_type.PNG)
        # self.driver.get_screenshot_as_file("img/xx.png")
        # with open("img/xx.png", "rb") as  f:
        #     allure
        allure.attach("截图",self.driver.get_screenshot_as_png(), allure.attach_type.PNG)



    

