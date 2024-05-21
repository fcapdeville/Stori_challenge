from behave import given
from pages.pages_background import PagesBackground


@given('Browser launched with mobile device characteristics')
def browser_launched(context):
    print('\033[92m' + "\nBrowser is launched with mobile device characteristics" + '\033[0m')
    pages_background = PagesBackground(context)
    pages_background.browser_launched()


@given('Navigate to challenge page')
def browser_and_page(context):
    print('\033[92m' + "\nNavigate to challenge page" + '\033[0m')
    context.driver.get("https://rahulshettyacademy.com/AutomationPractice/")
