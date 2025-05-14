from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from domain.Investment import Investment


def get_required_secure_nos(secure_no: str, input_elements: list[WebElement]):
    number_positions_required = []

    for input_element in input_elements:
        for char in input_element.text:
            if char.isdecimal():
                number_positions_required.append(int(char) - 1)
                break

    if len(number_positions_required) != 3:
        raise Exception("Could not find expected number of secure digits")

    return (
        secure_no[number_positions_required[0]],
        secure_no[number_positions_required[1]],
        secure_no[number_positions_required[2]],
    )


def get_stock_ticker(hl_row: WebElement) -> str:
    row_id = hl_row.get_attribute("id")

    if row_id is None:
        raise Exception("HL row ID could not be found - please investigate")

    split_row_id = row_id.split("-")

    if len(split_row_id) < 3:
        raise Exception("HL row ID format change - please investigate")

    return split_row_id[2]


def map_hl_row_to_investment(hl_row: WebElement) -> Investment:
    # TODO - could implement extra fields in future, beyond MVP functionality
    investment = Investment()
    ticker = get_stock_ticker(hl_row)
    name = hl_row.find_element(By.CLASS_NAME, "link-headline").text
    gain_loss = hl_row.find_element(By.CSS_SELECTOR, "[id^=live_price_gainpc]").text

    investment.ticker = ticker
    investment.name = name
    investment.gain_loss = float(gain_loss.strip())

    return investment
