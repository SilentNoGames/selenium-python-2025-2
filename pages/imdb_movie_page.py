from selenium.webdriver.common.by import By
from .base_page import BasePage
import time

class IMDbMoviePage(BasePage):
    MOVIE_NAME = (By.CLASS_NAME, 'hero__primary-text')
    MOVIE_CALIFICATION = (By.XPATH, '/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[2]/div[1]/div/div[1]/a/span/div/div[2]/div[1]/span[1]')
    
    def get_name(self):
        return self.find_element(self.MOVIE_NAME).text
    
    def get_calification(self):
        time.sleep(2)
        return self.find_element(self.MOVIE_CALIFICATION).text

