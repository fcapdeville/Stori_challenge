from subprocess import call


def before_all(context):
    # Initializing variables
    context.browser_name = context.config.userdata.get("browser", "chrome")
    if context.browser_name.lower() not in ["firefox", "chrome", "opera"]:
        print('\033[91m' + f"[ERROR] Browser provided is not supported: {context.browser_name}" + '\033[0m')
        raise AssertionError(f"[ERROR] Browser provided is not supported: {context.browser_name}")

    context.suggestion_class_counter = []
    context.dropdown_collector = []
    context.web_table_names = []
    context.web_table_fixed_names = []
    context.iframe_validation = False


def after_scenario(context, scenario):
    context.driver.quit()
