import argparse
import subprocess
import sys


def run_tests(browser):
    behave_command = (f"behave -f allure_behave.formatter:AllureFormatter -o Reports\\allure_result features -D "
                      f"browser={browser}")
    subprocess.run(behave_command, shell=True, check=True)

    allure_command = "allure generate Reports\\allure_result -o Reports\\allure_report --clean"
    subprocess.run(allure_command, shell=True, check=True)


if __name__ == "__main__":
    # Collecting arguments
    parser = argparse.ArgumentParser(description="Execution of Stori challenge with custom browser")
    parser.add_argument("--browser", type=str, default="chrome", help="Browsr for tests"
                                                                      "(chrome, firefox, opera)")

    args = parser.parse_args()
    run_tests(args.browser)
