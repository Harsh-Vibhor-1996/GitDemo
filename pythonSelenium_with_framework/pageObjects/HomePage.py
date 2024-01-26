

from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckOutPage


class HomePage:
    def __init__(self,driver):                                                     #creating constructor
        self.driver = driver
    shop=(By.XPATH, "//a[contains(@href,'shop')]")

    def shopItems(self):                                                           #name should start with lower case

       self.driver.find_element(*HomePage.shop).click()                             #we use '*' because we are using tuple and *deserialises
       checkOutPage = CheckOutPage(self.driver)                                     #integrating checkout page by creating checkOutPage method
       return checkOutPage
       #self.driver.find_element(By.XPATH, "//a[contains(@href,'shop')]").click()

