from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver

from features.testdata import geckodriver_path, chromedriver_path, operadriver_path


class PagesBackground:
    def __init__(self, context):
        self.context = context

    def browser_launched(self):
        """
        Preparing drivers and settings to use in Selenium
        :return: none
        """
        if self.context.browser_name.lower() == "firefox":
            firefox_options = FirefoxOptions()
            firefox_options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
            firefox_options.add_argument("--width=375")
            firefox_options.add_argument("--height=812")
            self.context.driver_path = geckodriver_path
            self.context.service = FirefoxService(executable_path=self.context.driver_path)
            self.context.driver = webdriver.Firefox(service=self.context.service, options=firefox_options)
        elif self.context.browser_name.lower() == "opera":
            opera_profile = r"C:\Users\capde\AppData\Roaming\Opera Software\Opera Stable"
            options = webdriver.ChromeOptions()
            options.add_argument("user-data-dir=" + opera_profile)
            options.binary_location = r"C:\Users\capde\AppData\Local\Programs\Opera\opera.exe"
            options = webdriver.ChromeOptions()
            options.add_argument('allow-elevated-browser')
            options.add_experimental_option('w3c', True)
            self.context.driver_path = operadriver_path
            self.context.driver = webdriver.Opera(executable_path=self.context.driver_path, options=options)
        elif self.context.browser_name.lower() == "chrome":
            chrome_options = Options()
            chrome_options.add_argument("--mobile-emulation=iPhone X")
            self.context.driver_path = chromedriver_path
            self.context.service = Service(executable_path=self.context.driver_path)
            self.context.driver = webdriver.Chrome(service=self.context.service, options=chrome_options)
        else:
            print('\033[91m' + f"[ERROR] Browser provided is not supported: {self.context.browser_name}" + '\033[0m')
            raise AssertionError(f"Browser provided is not supported: {self.context.browser_name}")
