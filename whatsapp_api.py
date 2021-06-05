from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep

# Parameters
WP_LINK = 'https://web.whatsapp.com'

class WhatsApp:
    def __init__(self):
        self.driver = self._setup_driver()
        self.driver.get(WP_LINK)
        print("Please scan the QR Code")

    @staticmethod
    def _setup_driver():
        print('Loading...')        
        from selenium import webdriver
        options = webdriver.ChromeOptions()
        options.add_argument(r'--user-data-dir=/home/whatsappuser/.config/google-chrome/Default/') #here is no <Default>!!
        driver = webdriver.Chrome(executable_path=r'chromedriver.exe', options=options) #selenium 4 preferes "options" -> your code is more up to date :-)
        driver.get('https://web.whatsapp.com')
        return driver

   

