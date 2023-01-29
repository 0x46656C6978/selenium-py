from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from .user_actions import UserAction

class Bigo():
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
            browser.implicitly_wait(30)
            browser.get('https://bigo.tv')

            WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__layout']/div/div[2]/div[2]/img"))).click()
            user = UserAction(browser)

            user.find_and_click("//*[@id='__layout']/div/header/div[2]/div[2]/button/span")
            user.wait(1)
            user.find_and_click("//*[@id='__layout']/div/header/div[3]/div/div[1]/div[3]/div[2]/a")
            user.wait(1)
            user.find_and_click("//*[@id='__layout']/div/header/div[3]/div/div[2]/div/div[2]/form/div[2]")
            user.wait(0.5)

            # Country
            user.fill_input("//*[@id='__layout']/div/header/div[3]/div/div[2]/div/div[2]/form/div[2]/div[1]/input", "Vietnam")
            user.wait(0.5)
            ul = browser.find_element(By.XPATH, "//*[@id='__layout']/div/header/div[3]/div/div[2]/div/div[2]/form/div[2]/div[2]/ul")
            elem = ul.find_element(By.XPATH, "//*[@id='__layout']/div/header/div[3]/div/div[2]/div/div[2]/form/div[2]/div[2]/ul/li[1]")
            action = ActionChains(browser)
            action.move_to_element(elem)
            action.click()
            action.perform()
            # Phone
            user.fill_input("//*[@id='__layout']/div/header/div[3]/div/div[2]/div/div[2]/form/div[4]/div/input", "0987654321")
            # Password
            user.fill_input("//*[@id='__layout']/div/header/div[3]/div/div[2]/div/div[2]/form/div[6]/input", "Admin123$")

            # Slide verification
            user.wait(0.5)
            elem = browser.find_element(By.XPATH, "//*[@id='captcha-box-register-bigo-captcha-element-bigo-captcha-sliderele']")

            action = ActionChains(browser)
            action.click_and_hold(elem).perform()
            tracks = range(30000)
            for i in tracks:
                action.move_to_element(elem).move_by_offset(i, 0).perform()
            action.pause(0.5).release().perform()

            user.wait(10)
        except Exception as e:
            print(e)
        except:
            print("exception????")
        finally:
            browser.quit()
    # end register
