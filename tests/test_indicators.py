from app.indicators import (
    moving_average,
    compare_moving_averages,
    relative_strength_index,
    exponential_moving_average,
    macd,
)


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


def test_rsi_flat_market():
    rows = []

    for _ in range(15):
        rows.append({"bitcoin": 100})

    rsi = relative_strength_index(rows, "bitcoin")

    assert rsi == 100.0

def test_exponential_moving_average_constant_prices():
    rows = [{"bitcoin": 100.0} for _ in range(30)]

    result = exponential_moving_average(rows, "bitcoin", 12)

    assert result == 100.0

def test_macd_constant_prices():
    rows = [{"bitcoin": 100.0} for _ in range(40)]

    result = macd(rows, "bitcoin")

    assert result["ema12"] == 100.0
    assert result["ema26"] == 100.0
    assert result["macd"] == 0.0
    assert result["signal"] == 0.0
    assert result["histogram"] == 0.0
