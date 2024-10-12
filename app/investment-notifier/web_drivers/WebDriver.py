from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from domain.Investment import Investment


class WebDriver:
    options = webdriver.FirefoxOptions()
    options.add_argument("-headless")
    sl_driver = webdriver.Firefox(options=options)

    def authenticate(self):
        raise NotImplementedError

    def get_all_time_percentage_change(self) -> str:
        raise NotImplementedError

    def get_investments(self) -> [Investment]:
        raise NotImplementedError

    def go_to(self, url: str) -> None:
        self.sl_driver.get(url)

    def set_implicit_wait(self, timeout: int = 2) -> None:
        self.sl_driver.implicitly_wait(timeout)

    def quit(self) -> None:
        self.sl_driver.quit()
