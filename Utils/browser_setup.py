from selenium import webdriver

PAGE = 'http://www.globalsqa.com/demo-site/'


def setup_browser(resolution: tuple = None, position: tuple = None):
    driver = webdriver.Chrome()
    driver.get(PAGE)
    if resolution:
        driver.set_window_size(*resolution)
    if position:
        driver.set_window_position(*position)
    return driver


def close_browser(driver: webdriver):
    driver.close()
    driver.quit()
