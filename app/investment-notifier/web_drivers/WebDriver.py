from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from domain.Investment import Investment


class WebDriver:
    chrome_options = Options()
    chrome_options.binary_location = './chrome/chromedriver.exe'
    sl_driver = webdriver.Chrome()

    def authenticate(self):
        raise NotImplementedError

    def get_all_time_percentage_change(self) -> str:
        raise NotImplementedError

    def get_investments(self) -> [Investment]:
        raise NotImplementedError

    def go_to(self, url: str) -> None:
        self.sl_driver.get(url)

    def wait(self, timeout: int = 2) -> None:
        self.sl_driver.implicitly_wait(timeout)

    def quit(self) -> None:
        self.sl_driver.quit()
