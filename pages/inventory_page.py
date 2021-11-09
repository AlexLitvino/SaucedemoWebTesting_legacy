from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):

    INVENTORY_CONTAINER = (By.ID, "inventory_container")

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def inventory_container(self):
        return self.element(InventoryPage.INVENTORY_CONTAINER)

    def is_page_displayed(self):
        return self.inventory_container.is_displayed()
