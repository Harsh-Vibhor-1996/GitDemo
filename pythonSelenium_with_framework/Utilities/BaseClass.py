import inspect

import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("setup")

class BaseClass:

    def verifylinkpresence(self,text):                                                                #as verifylinkpresence is inside the class it will have self parameter
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT,text)))

    def getLogger(self):                                              #code to get logfile
            loggerName = inspect.stack()[1][3]
            logger = logging.getLogger(loggerName)
            fileHandler = logging.FileHandler('logfile.log')
            formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
            fileHandler.setFormatter(formatter)

            logger.addHandler(fileHandler)  # filehandler object

            logger.setLevel(logging.DEBUG)
            return logger