import json

import requests
import typer
from rich import print
from rich.console import Console
from rich.table import Table

"""
The main function takes a stock ticker as input. Queries Yahoo finance API endpoint.
Displays the returned results to STDOUT in a table format.

TODO:
    * Perform validation on stock ticker. This should be a valid stock ticker.
    * Add support for multiple stock tickers.
    * Use a more stable documented API endpoint for fetching stock data.
    * Handle rate limiting by API endpoint.
"""

# Headers for GET method. Used to mimic a browser.
HEADERS = {
    "Connection": "keep-alive",
    "Expires": "-1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
}

# API endpoint for getting stock results
URL = "https://query1.finance.yahoo.com/v7/finance/quote?symbols={}"


def main(stock_ticker: str = typer.Argument("SNOW", help="Stock ticker symbol")):
    """Main function for displaying data for the given stock_ticker.

    Query Yahoo finance API end point for the given stock ticker.
    Print stock price data for the current day.

    Args:
        stock_ticker (str): String reprensting a code or symbol for a NASDAQ stock
    """
    print(
        f"Querying Yahoo finance API for stock ticker [italic bold blue]{stock_ticker}"
    )
    data = _get_stock_info(stock_ticker)
    _render_stock_info(data)


def _get_stock_info(stock_ticker: str) -> list:
    """Fetch data for the given stock_ticker.

    Returns a list of dict.
    Each dict item contains a days worth of data for the given stock ticker.

    Args:
        stock_ticker (str): String reprensting a code or symbol for a NASDAQ stock

    Returns:
        List of dict. Each dict element is stock data for the given ticker.

    Raises:
        Exception: If HTTP reponse status code is not 200
    """
    response = requests.get(url=URL.format(stock_ticker), headers=HEADERS)
    if response.status_code != 200:
        raise Exception(
            f"Received status code {response.status_code} when "
            f"querying for {stock_ticker}"
        )

    data = json.loads(response.text)
    _validate_stock_data(stock_ticker, data)
    return data["quoteResponse"]["result"]


def _validate_stock_data(stock_ticker: str, data: list):
    """Validate if there are any results from the API call.

    Args:
        stock_ticker (str): String reprensting a code or symbol for a NASDAQ stock
        data (list): List of dict. Each dict element contains data about a stock.

    Raises:
        Exception: If the payload contains no data for the given stock ticker.
    """
    if not data["quoteResponse"]["result"]:
        raise Exception(f"No stock data found for {stock_ticker}")


def _render_stock_info(data):
    """Render the stock data into a table format and print to console.

    Args:
        data (list): List of dict. Each dict element contains data about a stock.
    """
    table = Table(caption="Stock price dashboard")
    table.add_column("Name", style="green")
    table.add_column("Symbol", style="green")
    table.add_column("Price", style="green")
    table.add_column("Change", style="green")
    for d in data:
        name = d["longName"]
        symbol = d["symbol"]
        price = str(d["regularMarketPrice"])
        change = str(d["regularMarketChangePercent"])
        table.add_row(name, symbol, price, change)
    console = Console()
    console.print(table)


if __name__ == "__main__":
    typer.run(main)
