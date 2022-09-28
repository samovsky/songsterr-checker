from selenium.webdriver.common.by import By

class BasePageLocators():

    pass

class MainPageLocators(BasePageLocators):

    songSearchBox = (By.CLASS_NAME,'Cvu1qm')
    listOfSongs = (By.XPATH,"//div[@class='Ccm1w1 Ccm1n1']")