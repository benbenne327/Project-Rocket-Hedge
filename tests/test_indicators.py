from app.indicators import moving_average


def test_moving_average_uses_recent_rows():
    rows = [
        {"bitcoin": 10.0},
        {"bitcoin": 20.0},
        {"bitcoin": 30.0},
        {"bitcoin": 40.0},
        {"bitcoin": 50.0},
    ]

    result = moving_average(rows, "bitcoin", 3)

    assert result == 40.0

from app.indicators import compare_moving_averages


def test_buy_signal():

    buy_rows = [
        {"bitcoin": 10},
        {"bitcoin": 20},
        {"bitcoin": 30},
        {"bitcoin": 40},
        {"bitcoin": 50},
        {"bitcoin": 60},
        {"bitcoin": 70},
        {"bitcoin": 80},
        {"bitcoin": 90},
        {"bitcoin": 100},
    ]

    result = compare_moving_averages(buy_rows, "bitcoin")

    assert result["signal"] == "BUY"


