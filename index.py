from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from provider.bigo import Bigo
# import provider

chrome_opts = webdriver.ChromeOptions()
chrome_opts.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
chrome_opts.add_experimental_option('excludeSwitches', ['enable-logging'])

# download and put chrome driver into `drivers` directory
# then change the `chrome_driver_path`
chrome_driver_path = "C:\\Users\\nguye\\selenium-py\\drivers\\chromedriver.exe"
chrome_svc = ChromeService(ChromeDriverManager().install())

provider = Bigo(chrome_opts, chrome_svc, chrome_driver_path)
provider.register()
