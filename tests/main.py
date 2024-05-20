import sys
import argparse
from behave.__main__ import main as behave_main


if __name__ == "__main__":
    # Collecting arguments
    parser = argparse.ArgumentParser(description="Execution of Stori challenge with custom browser")
    parser.add_argument("--browser", type=str, default="chrome", help="Browsr for tests"
                                                                      "(chrome, firefox, opera)")

    args = parser.parse_args()
    sys.argv = [sys.argv[0], "--define", f"browser={args.browser}"]

    behave_main()
