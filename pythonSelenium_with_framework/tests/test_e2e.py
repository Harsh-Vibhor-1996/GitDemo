from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pytest

import Test_Data.test_data
from Utilities.BaseClass import BaseClass
from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.HomePage import HomePage

#@pytest.mark.usefixtures("setup")                           #no need to use as we are using base class
class TestOne(BaseClass):                                   #inheriting baseclass (parent class to child class.

    def test_e2e(self,getData):                                     #to define anything underclass should have self parameter
        log = self.getLogger()
        homePage= HomePage(self.driver)
        self.driver.implicitly_wait(5)

        checkoutPage = homePage.shopItems()                                            # used a part of href value in Xpath    #self not required in shopItems() as we are calling it from object 'homePage' name not class name 'HomePage'.
        log.info("getting all the card titles")
        #checkOutPage = CheckOutPage(self.driver)
        checkoutPage.select_mobile(getData['mobileName'])

        checkoutPage.checkout_button()

        confirm_page = checkoutPage.checkout_button()
        log.info("Entering country name as ind")
        confirm_page.enter_country(getData['entered_country_name'])
        self.verifylinkpresence(getData['country_presence'])
        confirm_page.select_india()
        confirm_page.final_purchase()

    @pytest.fixture(params =Test_Data.test_data.testData.page_data)
    def getData(self,request):
        return request.param


