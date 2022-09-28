import element
import locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePage():
     
    def __init__(self,driver):
        self.driver = driver

    def doesTitleMatch(self):
        return 'Songsterr' in self.driver.title

class MainPage(BasePage):
    
    def foundSongs(self):
        
        try:
            WebDriverWait(self.driver,3).until(EC.presence_of_element_located(locators.MainPageLocators.listOfSongs))
            return True

        except:
            return False

    searchSong = element.SongSearchElement()

