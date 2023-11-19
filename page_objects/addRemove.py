from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from utilities.BaseClass import BaseClass


class AddRemoveElement(BaseClass):

    def __init__(self, driver):
        self.driver = driver
        self._wait = WebDriverWait(self.driver, 10)
        self._action = ActionChains(self.driver)

    ADD_REMOVE_LINK = (By.LINK_TEXT, "Add/Remove Elements")
    ADD_ELEMENT_BTN = (By.TAG_NAME, "button")
    DELETE_BTN = (By.CLASS_NAME, "added-manually")

    def navigate_to_add_remove_page(self):
        self.wait_for(self.ADD_REMOVE_LINK).click()
    
    def click_add_element_button(self):
        self.wait_for(self.ADD_ELEMENT_BTN).click()

    def check_delete_button(self):
        try: 
            return self.wait_for(self.DELETE_BTN)
        except TimeoutException:
            return "No Delete Button"

    def click_delete_button(self):
        self.find(self.DELETE_BTN).click()