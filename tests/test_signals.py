from app.signals import build_signal


def test_strong_buy():
    analysis = {"trend": "UP"}
    rsi = 25
    macd = {"histogram": 10}
    bb = {"percent_b": -0.1}

    result = build_signal(analysis, rsi, macd, bb)

    assert result["recommendation"] == "STRONG BUY"


def test_buy():
    analysis = {"trend": "UP"}
    rsi = 40
    macd = {"histogram": 0}
    bb = {"percent_b": 0.5}

    result = build_signal(analysis, rsi, macd, bb)

    assert result["recommendation"] == "BUY"


def test_hold():
    analysis = {"trend": "SIDEWAYS"}
    rsi = 50
    macd = {"histogram": 0}
    bb = {"percent_b": 0.5}

    result = build_signal(analysis, rsi, macd, bb)

    assert result["recommendation"] == "HOLD"


def test_sell():
    analysis = {"trend": "DOWN"}
    rsi = 60
    macd = {"histogram": 0}
    bb = {"percent_b": 0.5}

    result = build_signal(analysis, rsi, macd, bb)

    assert result["recommendation"] == "SELL"


def test_strong_sell():
    analysis = {"trend": "DOWN"}
    rsi = 90
    macd = {"histogram": -10}
    bb = {"percent_b": 1.2}

    result = build_signal(analysis, rsi, macd, bb)

    assert result["recommendation"] == "STRONG SELL"
