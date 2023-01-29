from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .user_actions import UserAction

class Google():
    chrome_options = None
    chrome_service = None
    chrome_driver_path = None

    def __init__(self, options: Options, service: ChromeService, driver_path):
        self.chrome_options = options
        self.chrome_service = service
        self.chrome_driver_path = driver_path


    def register(self):
        try:
            browser = webdriver.Chrome(service=self.chrome_service, options=self.chrome_options, executable_path=self.chrome_driver_path)
            browser.maximize_window()
            browser.implicitly_wait(10)
            browser.get('https://accounts.google.com/signup/v2/webcreateaccount?hl=en')

            # Stage 1, find the way to register page
            WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located)
            user = UserAction(browser)

            user.find_and_click("//*[text()='Create account']")
            user.find_and_click("//*[text()='For my personal use']")
            user.wait(2)

            # Stage 2, fill register information
            user.fill_input("//*[@id='firstName']", "John")
            user.fill_input("//*[@id='lastName']", "Cena")
            user.fill_input("//*[@id='username']", "csgofaceit10kelo")
            user.fill_input("//*[@id='passwd']/div[1]/div/div[1]/input", "Admin123$%^")
            user.fill_input("//*[@id='confirm-passwd']/div[1]/div/div[1]/input", "Admin123$%^")
            user.find_and_click("//*[text()='Next']")

            # Stage 3, fill phone number and get OTP
            user.fill_input("//*[@id='phoneNumberId']", "0987654321")
            user.wait(1)
            user.find_and_click("//*[@id='view_container']/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span")

            # Wait 4s before close
            user.wait(4)
        except Exception as e:
            print(e)
        except:
            print("exception????")
        finally:
            browser.quit()
    # end register
