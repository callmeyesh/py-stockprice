# py-stockprice
<!-- ABOUT THE PROJECT -->
## About The Project

Simple command line tool for displaying stock data. This project uses Yahoo finance API to get the stock information and prints it to the command line.

### Main Features
- Management of dependencies with [Poetry](https://python-poetry.org)
- Check for the pythonic style with [flake8](https://flake8.pycqa.org), [black](https://black.readthedocs.io) and [isort](https://pycqa.github.io/isort)
- Code checking with [pytest](https://pytest.org)
- Code report with [codecov](https://codecov.io)
- CLI arg parsing support using [typer](https://typer.tiangolo.com/)
- Stock data rendering using [Rich](https://github.com/Textualize/rich)

<!-- GETTING STARTED -->
## Getting Started

Please follow these instructions to execute the tool inside a Docker container or locally using Pottery.

### Prerequisites

* Docker: https://docs.docker.com/get-docker/
* Pottery (optional) https://python-poetry.org/docs/#installation

### Local development using Docker

1. Clone the repo and `cd` into it.
   ```sh
   git clone git@github.com:callmeyesh/py-stockprice.git
   cd py-stockprice
   ```
2. Build the Docker image using the following command.
    ```sh
    docker build -t py-stockprice:v1 .
    ```
3. Start a container using the image created
   ```sh
    docker run -it py-stockprice:v1 sh
   ```
4. Run the script using `make`. It uses default stock ticker `(SNOW)` while executing the script.
   ```sh
    make run
   ```
5. Run the script using `pottery` by passing a custom stock ticker.
   ```sh
    poetry run python py_stockprice/main.py TSLA
   ```
6. To run test cases (HTML coverage report should be generated inside `htmlcov` folder).
   ```sh
    make tests
   ```

### Local development using Pottery
1. Clone the repo and `cd` into it.
   ```sh
   git clone git@github.com:callmeyesh/py-stockprice.git
   cd py-stockprice
   ```
2. Install dependencies
   ```sh
   make install
   ```
3. Run the script using `pottery` by passing a custom stock ticker. If no stock ticker is passed defaults to using `SNOW` as ticker.
   ```sh
    poetry run python py_stockprice/main.py TSLA
   ```
4. To run test cases (HTML coverage report should be generated inside `htmlcov` folder).
   ```sh
    make tests
   ```

<!-- Limitations -->
## Limitations

- [ ] Use a stable well tested API to get stock data. Yahoo finance API is not documented and seems to be inconsistent.
- [ ] Perform validation on stock ticker.
    - [ ] Stock ticker should be a valid NASDAQ stock ticker.
- [ ] Better API validation. Currently just checking for status code != 200.
- [ ] Add support for multiple stock tickers.
- [ ] Handle rate limiting when fetching stock data.
