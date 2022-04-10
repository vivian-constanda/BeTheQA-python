from Utils.browser_setup import setup_browser, close_browser
import time
from pages.sample_page.sample_page_page import SamplePagePage

driver = setup_browser()
experience="3-5"
name="Popa Ion"
email="popa@yahoo.com"
website="weather.com"
sample_page_page = SamplePagePage(driver,navigate=True)
sample_page_page.upload_file(file_path='C:/Users/Vivian/Desktop/pom session 5/pages/resources/upload.text')
# sample_page_page.select_experience(experience)
# sample_page_page.fillin_name(name)
# sample_page_page.fillin_email(email)
# sample_page_page.fillin_website(website)
sample_page_page.fillform('C:/Users/Vivian/Desktop/pom session 5/pages/resources/upload.text',name, email, website,experience)
sample_page_page.submit_button()
time.sleep(5)
close_browser(driver)

