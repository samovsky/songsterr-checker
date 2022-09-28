import locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseSearchElement():

    def __set__(self,obj,value):
        self.driver = obj.driver
        
        WebDriverWait(self.driver,3).until(EC.presence_of_element_located(self.locator))
        entryBox = self.driver.find_element(*self.locator)
        entryBox.send_keys(value)

class SongSearchElement(BaseSearchElement):

    locator = locators.MainPageLocators.songSearchBox