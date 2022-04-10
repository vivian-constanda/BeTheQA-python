from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.select import Select

from Utils.browser_setup import setup_browser


#class BaseLocators():
#   PAGE_BUTTON = (By.XPATH, '//a[text()="{}"]')
#   TABS = (PAGE_BUTTON[0], PAGE_BUTTON[1].format('Tabs'))
#    DialogBox = (PAGE_BUTTON[0], PAGE_BUTTON[1].format('DialogBox'))
#   DropDown = (PAGE_BUTTON[0], PAGE_BUTTON[1].format('DropDown'))
#   ProgressBar = (PAGE_BUTTON[0], PAGE_BUTTON[1].format('ProgressBar'))

class BaseLocators():
    pass

class BasePage():
    PAGE=''

    def __init__(self, driver: WebDriver, navigate=False):
        self.driver=driver
        if not driver:
            driver = setup_browser()
        if navigate:
            driver.get(self.PAGE)

    #define a method to switch to an iframe
    def switch_to_iframe(self,iframeLocator):
        iframe=self.driver.find_element(*iframeLocator)
        self.driver.switch_to.frame(iframe)

    def select_option_from_dropdown(self, locator, value):
        dropdown=Select(self.driver.find_element(*locator))
        dropdown.select_by_visible_text(value)




