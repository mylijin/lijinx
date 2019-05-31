import time

import allure

from page.page import Page
from base.bage_one import init
import pytest


import yaml

# def li():
#
#      with open("./data.yaml",'r') as f:
#          data = yaml.load(f)
#          for i in data.values() :
#              if i ==data.get("test_monkey"):
#                  return  i
#
#
#
#
#
# def jin():
#     ll = []
#     for j in li().values():
#         ll.append(j)
#     return ll
#
# # print(jin())
#
# def xing():
#     jj = [[],[]]
#
#     z= 0
#     for x  in jin():
#         jj[z].append(x.get("phonea"))
#         jj[z].append(x.get("content"))
#         z +=1
#
#
#
#
#     return jj
#
#


def analyze_data( case_key):
    with open("./data.yaml", "r", encoding='utf-8') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)[case_key]
        data_list = list()
        data_list.extend(data.values())
        return data_list




# jin()

class Test1:

    def setup(self):
        self.driver = init()
        self.page = Page(self.driver)

    @pytest.mark.parametrize("ages",analyze_data("test_monkey"))
    def test1(self,ages):
        self.page.pageone.newconcat()
        self.page.pagetwo.name(ages["phone"])
        self.page.pagetwo.phone(ages["content"])
        time.sleep(2)

    def teardown(self):
        self.driver.close_app()

