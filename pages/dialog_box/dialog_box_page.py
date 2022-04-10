from Utils.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class DialogBoxLocators:

    TITLE=(By.XPATH,'//div[@class="page_heading"]/h1')
    CONFIRMATION_BOX=(By.XPATH,'//li[@id="Confirmation Box"]')
    SECTION_IFRAME=(By.XPATH, "//iframe[@src='../../demoSite/practice/dialog/modal-form.html']")
    CREATE_NEW_USER_BUTTON=(By.XPATH, "//button[@id='create-user']")
    NAME_FIELD=(By.XPATH, "//input[@id='name']")
    EMAIL_FIELD=(By.XPATH, "//input[@id='email']")
    PASSWORD_FIELD=(By.XPATH, "//input[@id='password']")
    CREATE_AN_ACCOUNT_BUTTON=(By.XPATH, '//button[text()="Create an account"]')
    ROW_LOCATOR=(By.XPATH, '//table/tbody/tr[{}]/td[{}]')

class DialogBoxPage(BasePage):
    PAGE='http://www.globalsqa.com/demo-site/dialog-boxes/'

    def __init__(self,driver ,navigate):
        super().__init__(driver,navigate)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(DialogBoxLocators.CONFIRMATION_BOX))

    def create_new_user(self,name=None, email=None, password=None):
        self.switch_to_iframe(DialogBoxLocators.SECTION_IFRAME)
        self.driver.find_element(*DialogBoxLocators.CREATE_NEW_USER_BUTTON).click()
        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable(DialogBoxLocators.CREATE_AN_ACCOUNT_BUTTON))
        if name:
            self.driver.find_element(*DialogBoxLocators.NAME_FIELD).clear()
            self.driver.find_element(*DialogBoxLocators.NAME_FIELD).send_keys(name)
        if email:
            self.driver.find_element(*DialogBoxLocators.EMAIL_FIELD).clear()
            self.driver.find_element(*DialogBoxLocators.EMAIL_FIELD).send_keys(email)
        if password:
            self.driver.find_element(*DialogBoxLocators.PASSWORD_FIELD).clear()
            self.driver.find_element(*DialogBoxLocators.PASSWORD_FIELD).send_keys(password)
        self.driver.find_element(*DialogBoxLocators.CREATE_AN_ACCOUNT_BUTTON).click()
        import time; time.sleep(10)

    def check_row(self,row_number,name,email,password):
        element=self.driver.find_element(
            DialogBoxLocators.ROW_LOCATOR[0],
            DialogBoxLocators.ROW_LOCATOR[1].format(str(row_number),'1'))
        if not element.text==name:
            return False
        element = self.driver.find_element(
        DialogBoxLocators.ROW_LOCATOR[0],
        DialogBoxLocators.ROW_LOCATOR[1].format(str(row_number),'2'))
        if not element.text == email:
            return False
        element = self.driver.find_element(
        DialogBoxLocators.ROW_LOCATOR[0],
        DialogBoxLocators.ROW_LOCATOR[1].format(str(row_number),'3'))
        if not element.text == password:
            return False

        return True

    #
    # #defne a method to click on sections
    # def click_section(self,section):
    #     self.switch_to_iframe(TabsLocators.SECTION_IFRAME)
    #     self.driver.find_element(*section).click()
    #
    #
    # #define a method to return the text
    # def get_paragrapgh_text(self,paragraph):
    #     WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(paragraph))
    #     paragraph_element=self.driver.find_element(*paragraph)
    #     return paragraph_element.text



