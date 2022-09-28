from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import unittest
import page
import time

class SongsterrChecker(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('https://www.songsterr.com/')

    def test_song_presence(self):
        main_page = page.MainPage(self.driver)

        if main_page.doesTitleMatch() == False:
            raise AssertionError('title does not match')
            
        main_page.searchSong = 'Curents'
        time.sleep(1)

        self.assertTrue(main_page.foundSongs(),'no songs were found for set keyword')

    def tearDown(self):

        self.driver.quit()

if __name__ == '__main__':
    SongsterrChecker()
    unittest.main()