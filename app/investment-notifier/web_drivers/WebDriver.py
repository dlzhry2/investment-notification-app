from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from tempfile import mkdtemp
from collections.abc import Iterable

from domain.Investment import Investment


class WebDriver:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-dev-tools")
    chrome_options.add_argument("--no-zygote")
    chrome_options.add_argument("--single-process")
    chrome_options.add_argument(f"--user-data-dir={mkdtemp()}")
    chrome_options.add_argument(f"--data-path={mkdtemp()}")
    chrome_options.add_argument(f"--disk-cache-dir={mkdtemp()}")
    chrome_options.add_argument("--remote-debugging-pipe")
    chrome_options.add_argument("--verbose")
    chrome_options.add_argument("--log-path=/tmp")
    chrome_options.binary_location = "/opt/chrome/chrome-linux64/chrome"

    service = Service(
        executable_path="/opt/chrome-driver/chromedriver-linux64/chromedriver",
        service_log_path="/tmp/chromedriver.log",
    )
    sl_driver = webdriver.Chrome(service=service, options=chrome_options)

    def __authenticate(self):
        raise NotImplementedError

    def get_all_time_percentage_change(self) -> str:
        raise NotImplementedError

    def get_investments(self) -> Iterable[Investment]:
        raise NotImplementedError

    def go_to(self, url: str) -> None:
        self.sl_driver.get(url)

    def set_implicit_wait(self, timeout: int = 2) -> None:
        self.sl_driver.implicitly_wait(timeout)

    def quit(self) -> None:
        self.sl_driver.quit()
