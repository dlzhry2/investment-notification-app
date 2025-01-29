import os

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from domain.Investment import Investment
from web_drivers.WebDriver import WebDriver
from web_drivers.util.HL_helper import get_required_secure_nos, map_hl_row_to_investment


class HLDriver(WebDriver):
    authenticated: bool = False

    def __init__(self):
        self.set_implicit_wait(5)

    def authenticate(self) -> None:
        user_name = os.getenv("LOGIN_USER_NAME")
        date_of_birth = os.getenv("LOGIN_DOB")

        # First step auth
        self.go_to("https://online.hl.co.uk/my-accounts/login-step-one")

        # Intermittent error: maybe session is persisted
        try:
            self.sl_driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
        except NoSuchElementException as e:
            print(f"The cookie banner was not found {e.msg}")

        self.sl_driver.find_element(By.NAME, "username").send_keys(user_name)
        self.sl_driver.find_element(By.NAME, "date-of-birth").send_keys(date_of_birth)
        self.sl_driver.find_element(By.CLASS_NAME, "tertiary-button-large").click()

        # Should do local .env and SSM in AWS
        user_password = os.getenv("LOGIN_PASSWORD")
        user_secure_no = os.getenv("LOGIN_SECURE_NO")

        # Second step auth
        self.sl_driver.find_element(By.ID, "online-password-verification").send_keys(user_password)
        secure_numbers_required = self.sl_driver.find_elements(By.CLASS_NAME, "secure-number-container__label")
        no_one, no_two, no_three = get_required_secure_nos(user_secure_no, secure_numbers_required)
        self.sl_driver.find_element(By.NAME, "secure-number[1]").send_keys(no_one)
        self.sl_driver.find_element(By.NAME, "secure-number[2]").send_keys(no_two)
        self.sl_driver.find_element(By.NAME, "secure-number[3]").send_keys(no_three)
        self.sl_driver.find_element(By.CLASS_NAME, "tertiary-button-large").click()

        self.authenticated = True

    def get_all_time_percentage_change(self) -> str:
        if not self.authenticated:
            self.authenticate()

        self.go_to("https://online.hl.co.uk/my-accounts")
        self.sl_driver.find_element(By.CLASS_NAME, "product-name").click()
        hack = self.sl_driver.page_source

        percentage_change = self.sl_driver.find_element(By.ID, "gainpc_total").text
        return f"{percentage_change.strip()} %"

    def get_investments(self) -> [Investment]:
        if not self.authenticated:
            self.authenticate()

        self.go_to("https://online.hl.co.uk/my-accounts")
        self.sl_driver.find_element(By.CLASS_NAME, "product-name").click()
        self.set_implicit_wait()
        hack = self.sl_driver.page_source

        investment_rows = self.sl_driver.find_elements(By.CSS_SELECTOR, "[id^=ls-row-]")
        investments: [Investment] = []

        for investment_row in investment_rows:
            mapped_investment = map_hl_row_to_investment(investment_row)
            investments.append(mapped_investment)

        return investments
