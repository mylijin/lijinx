from page.page_one import  PageOne
import pytest
from  page.page_two import PageTwo
class Page:

    def __init__(self,driver):
        self.driver = driver

    @property
    def pageone(self):
        return PageOne(self.driver)
    @property
    def pagetwo(self):
        return PageTwo(self.driver)
