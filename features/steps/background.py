from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from behave import given


@given('Browser launched with mobile device characteristics')
def browser_launched(context):
    print('\033[92m' + "\nBrowser is launched with mobile device characteristics" + '\033[0m')
    if context.browser_name.lower() == "firefox":
        print('\033[92m' + "Firefox TBD" + '\033[0m')
        exit()
    elif context.browser_name.lower() == "opera":
        print('\033[92m' + "Opera TBD" + '\033[0m')
        exit()
    elif context.browser_name.lower() == "chrome":
        chrome_options = Options()
        chrome_options.add_argument("--mobile-emulation=iPhone X")
        context.driver_path = "E:/Chromedriver/chromedriver.exe"
        context.service = Service(executable_path=context.driver_path)
        context.driver = webdriver.Chrome(service=context.service, options=chrome_options)
    else:
        print('\033[91m' + "[ERROR] Browser provided is not supported: " + context.browser_name + '\033[0m')
        exit()


@given('Navigate to challenge page')
def browser_and_page(context):
    print('\033[92m' + "\nNavigate to challenge page" + '\033[0m')
    context.driver.get("https://rahulshettyacademy.com/AutomationPractice/")
