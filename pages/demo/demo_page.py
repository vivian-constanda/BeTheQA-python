from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pages.dialog_box.dialog_box_page import DialogBoxPage
from pages.tabs.tabs_page import TabsPage
from Utils.base_page import BasePage


class DemoLocators():
    PAGE_BUTTON = (By.XPATH, '//a[text()="{}"]')
    TABS = (PAGE_BUTTON[0], PAGE_BUTTON[1].format('Tabs'))
    DIALOG_BOX = (PAGE_BUTTON[0], PAGE_BUTTON[1].format('DialogBox'))
    Drop_Down = (PAGE_BUTTON[0], PAGE_BUTTON[1].format('DropDown'))
    Progress_Bar = (PAGE_BUTTON[0], PAGE_BUTTON[1].format('ProgressBar'))


class DemoPage(BasePage):
    PAGE = 'http://www.globalsqa.com/demo-site/'

    def __init__(self, driver: WebDriver, navigate):
        super().__init__(driver, navigate)
        # WebDriverWait(driver, 5).until(EC.element_to_be_clickable(TabsLocators.ToggleIcons))

    def click_tabs(self):
        tabs_button = self.driver.find_element(*DemoLocators.TABS)
        tabs_button.click()
        return TabsPage(self.driver, navigate=False)

    def click_dialog_box(self):
        dialog_box_button=self.driver.find_element(*DemoLocators.DIALOG_BOX)
        dialog_box_button.click()
        return DialogBoxPage(self.driver,navigate=False)
