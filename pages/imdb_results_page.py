from selenium.webdriver.common.by import By
from .base_page import BasePage

class IMDBResultsPage(BasePage):
    FIRST_RESULT_LINK = (By.CLASS_NAME, 'ipc-metadata-list-summary-item__t')

    def click_first_result(self):
        self.click(self.FIRST_RESULT_LINK)

