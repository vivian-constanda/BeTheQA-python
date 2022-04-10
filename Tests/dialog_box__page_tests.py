#from Utils.browser_setup import setup_browser, close_browser
#from pages.demo.demo_page import DemoPage
#from pages.tabs.tabs_page import TabsLocators
from Utils.browser_setup import setup_browser,close_browser
from pages.demo.demo_page import DemoPage

expected_text="Sed non urna. Donec et ante. Phasellus eu ligula. Vestibulum sit amet purus. Vivamus hendrerit, dolor at aliquet laoreet, mauris turpis porttitor velit, faucibus interdum tellus libero ac justo. Vivamus non quam. In suscipit faucibus urna."
driver = setup_browser()
demo_page = DemoPage(driver,navigate=True)
dialog_box_page=demo_page.click_dialog_box()
dialog_box_page.create_new_user(name='admin',email='test@somehting.com',password='password')
assert dialog_box_page.check_row(2, name='admin',email='test@somehting.com',password='password')
close_browser(driver)

# tabs_page.click_section(TabsLocators.SECTION_2)
# actual_text=tabs_page.get_paragrapgh_text(TabsLocators.SECTION_2_PARAGRAPH)
# assert actual_text== expected_text


