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

def test_sell_signal():
    sell_rows = [
        {"bitcoin": 100},
        {"bitcoin": 90},
        {"bitcoin": 80},
        {"bitcoin": 70},
        {"bitcoin": 60},
        {"bitcoin": 50},
        {"bitcoin": 40},
        {"bitcoin": 30},
        {"bitcoin": 20},
        {"bitcoin": 10},
    ]

    result = compare_moving_averages(sell_rows, "bitcoin")

    assert result["signal"] == "SELL"
    assert result["trend"] == "DOWN"


def test_hold_signal():
    hold_rows = [
        {"bitcoin": 100},
        {"bitcoin": 100},
        {"bitcoin": 100},
        {"bitcoin": 100},
        {"bitcoin": 100},
        {"bitcoin": 100},
        {"bitcoin": 100},
        {"bitcoin": 100},
        {"bitcoin": 100},
        {"bitcoin": 100},
    ]

    result = compare_moving_averages(hold_rows, "bitcoin")

    assert result["signal"] == "HOLD"
    assert result["trend"] == "SIDEWAYS"


def test_compare_moving_averages_rejects_empty_history():
    try:
        compare_moving_averages([], "bitcoin")
    except ValueError as error:
        assert str(error) == "Price history cannot be empty"
    else:
        raise AssertionError("Expected ValueError for empty price history")

from app.indicators import relative_strength_index

def test_placeholder_rsi():
    rows = [{"bitcoin": 100}]

    rsi = relative_strength_index(rows, "bitcoin")

    assert rsi == 50.0

