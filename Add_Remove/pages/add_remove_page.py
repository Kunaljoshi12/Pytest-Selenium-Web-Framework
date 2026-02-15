from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class AddRemovePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.ADD_BUTTON = (By.XPATH, "//button[text()='Add Element']")
        self.DELETE_BUTTON = (By.CLASS_NAME, "added-manually")
        self.URL = "https://the-internet.herokuapp.com/add_remove_elements/"

    def open(self):
        self.driver.get(self.URL)

    def add_element(self):
        self.click(self.ADD_BUTTON)

    def remove_element(self):
        self.click(self.DELETE_BUTTON)

    def get_delete_button_count(self):
        return len(self.find_elements(self.DELETE_BUTTON))