
from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:
    def __init__(self,driver):
        self.driver = driver

    mobile_items =(By.XPATH, '//app-card/div')
    mobile_name  = (By.XPATH,'div/h4/a')
    checkout_Button = (By.XPATH, ' //li/a[contains(@class,"btn-primary")] ')
    def getmobileItems(self):

       return self.driver.find_elements(*CheckOutPage.mobile_items)

    def select_mobile(self,mobile_name):
        Mobile_Items = CheckOutPage.getmobileItems(self)
        for Mobile_Item in Mobile_Items:                                                    # from here on we will use Mobile_Item.abc not driver .abc
            Mobile_Name = Mobile_Item.find_element(By.XPATH, 'div/h4/a')                    # not used the entire XPATH only 'div/h4/a'

            if Mobile_Name.text == mobile_name:
                return Mobile_Item.find_element(By.XPATH, 'div[2]/button').click()

    def checkout_button(self):
        self.driver.find_element(*CheckOutPage.checkout_Button).click()
        self.driver.find_element(By.XPATH, '(//td/button)[3]').click()
        confirm_Page = ConfirmPage(self.driver)
        return confirm_Page
