from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class WebDriver:
    chrome_options = Options()
    chrome_options.binary_location = './chrome/chromedriver.exe'
    sl_driver = webdriver.Chrome()

    def authenticate(self):
        raise NotImplementedError

    def go_to(self, url: str) -> None:
        self.sl_driver.get(url)

    def wait(self, timeout: int = 2) -> None:
        self.sl_driver.implicitly_wait(timeout)

    def quit(self) -> None:
        self.sl_driver.quit()
