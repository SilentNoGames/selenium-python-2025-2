from selenium.webdriver.common.by import By
from .base_page import BasePage

class LastFmArtistPage(BasePage):

    LATEST_RELEASE = (By.CLASS_NAME,'artist-header-featured-items-item-date')

    def get_latest_release(self):
        return self.find_element(self.LATEST_RELEASE).text