import requests
from bs4 import BeautifulSoup

class CurrencyConverter:
    def __init__(self):
        self.exchange_rate = self.get_exchange_rate()

    def get_exchange_rate(self):
        url = "https://bank.gov.ua/ua/markets/exchangerates"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        usd_rate = soup.find("td", text="Долар США").find_next_sibling("td").text
        return float(usd_rate.replace(',', '.'))

    def convert_to_usd(self, amount_uah):
        return amount_uah / self.exchange_rate


if __name__ == "__main__":
    converter = CurrencyConverter()
    amount_uah = float(input("Введіть кількість гривень: "))
    amount_usd = converter.convert_to_usd(amount_uah)
    print(f"{amount_uah} гривень = {amount_usd:.2f} доларів США")