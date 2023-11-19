from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from utilities.BaseClass import BaseClass


class ContextMenu(BaseClass):

    def __init__(self, driver):
        self.driver = driver
        self._wait = WebDriverWait(self.driver, 10)
        self._action = ActionChains(self.driver)

    CONTEXT_MENU = (By.LINK_TEXT, "Context Menu")
    CONTEXT_BOX = (By.ID, "hot-spot")
    PAGE_TITLE = (By.XPATH, "//div[@class='example']/h3")


    def navigate_to_context_menu_page(self):
        self.wait_for(self.CONTEXT_MENU).click()

    def right_click_context_menu(self):
        context_menu = self.find(self.CONTEXT_BOX)
        self.context_click(context_menu).perform()

    def check_alert_message(self):
        return self.alert().text

    def accept_alert(self):
        return self.alert().accept()

    def alert_is_accepted(self):
        return self.wait_for(self.PAGE_TITLE).text