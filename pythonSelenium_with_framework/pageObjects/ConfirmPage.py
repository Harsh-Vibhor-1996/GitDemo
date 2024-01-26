from selenium.webdriver.common.by import By

class ConfirmPage:
    def __init__(self,driver):
        self.driver = driver
    enter_country_name = (By.CSS_SELECTOR, '#country')
    india = (By.LINK_TEXT, 'India')
    checkbox = (By.XPATH, '//label[@for="checkbox2"]')
    purchase = (By.XPATH, '//input[@value="Purchase"]')

    def enter_country(self,country):
        return self.driver.find_element(*ConfirmPage.enter_country_name).send_keys(country)

    def select_india(self):
        return self.driver.find_element(*ConfirmPage.india).click()        #works even without using return

    def final_purchase(self):
        self.driver.find_element(*ConfirmPage.checkbox).click()
        self.driver.find_element(*ConfirmPage.purchase).click()