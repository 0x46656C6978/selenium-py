from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class UserAction():
    browser = None

    def __init__(self, browser: webdriver.Chrome) -> None:
        self.browser = browser

    def fill_input(self, path, value):
        e = self.browser.find_element(By.XPATH, path)
        e.send_keys(value)

    def find_and_click(self, path):
        e = self.browser.find_element(By.XPATH, path)
        e.click()

    def find_and_click_text(self, text):
        e = self.browser.find_element(By.LINK_TEXT, text)
        e.click()

    def wait(self, duration):
        time.sleep(duration)
