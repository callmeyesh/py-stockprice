import json
from unittest.mock import MagicMock, patch

import pytest
import typer
from typer.testing import CliRunner

from py_stockprice.main import _get_stock_info, _validate_stock_data, main

app = typer.Typer()
app.command()(main)
runner = CliRunner()


@patch("py_stockprice.main.requests")
def test_get_stock_info_exception(mock_requests):
    """Test if exception is raised when status code is not 200."""
    mock_response = MagicMock()
    mock_response.status_code = 400
    mock_response.json.return_value = {}
    mock_requests.get.return_value = mock_response
    exception_message = "Received status code 400 when querying for FOO"
    with pytest.raises(Exception, match=exception_message) as _:
        _get_stock_info("FOO")


@patch("py_stockprice.main.requests")
def test_get_stock_info_success(mock_requests):
    """Test if result for the stock is returned succesfully."""
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.text = json.dumps({"quoteResponse": {"result": [{"foo": "bar"}]}})
    mock_requests.get.return_value = mock_response
    assert _get_stock_info("FOO") == [{"foo": "bar"}]


def test_validate_stock_data_exception():
    """Test if exception is raised if there is no result data present."""
    test_data = {"quoteResponse": {"result": []}}
    exception_message = "No stock data found for FOO"
    with pytest.raises(Exception, match=exception_message) as _:
        _validate_stock_data("FOO", test_data)


def test_py_stockprice_success():
    """Full functinal test case by calling a valid stock ticker."""
    result = runner.invoke(app, ["TSLA"])
    assert result.exit_code == 0


def test_py_stockprice_error():
    """Full functinal test case by calling an invalid stock ticker."""
    result = runner.invoke(app, ["FOO"])
    assert result.exit_code == 1
