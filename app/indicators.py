import math

def moving_average(rows, coin, period=10):
 recent = rows[-min(period, len(rows)):]
 return sum(r[coin] for r in recent) / len(recent)

def compare_moving_averages(rows, coin, short_period=5, long_period=10):
    if not rows:
        raise ValueError("Price history cannot be empty")

    short_average = moving_average(rows, coin, short_period)
    long_average = moving_average(rows, coin, long_period)
    difference_percent = ((short_average - long_average) / long_average) * 100

    if difference_percent >= 0.10:
        trend = "UP"
        signal = "BUY"
    elif difference_percent <= -0.10:
        trend = "DOWN"
        signal = "SELL"
    else:
        trend = "SIDEWAYS"
        signal = "HOLD"

    return {
        "short_average": short_average,
        "long_average": long_average,
        "difference_percent": difference_percent,
        "trend": trend,
        "signal": signal,
    }

def relative_strength_index(rows, coin, period=14):
    if len(rows) < 2:
        return 50.0

    gains = []
    losses = []

    recent = rows[-(period + 1):]

    for i in range(1, len(recent)):
        change = recent[i][coin] - recent[i - 1][coin]

        if change > 0:
            gains.append(change)
            losses.append(0)
        else:
            gains.append(0)
            losses.append(abs(change))

    average_gain = sum(gains) / len(gains)
    average_loss = sum(losses) / len(losses)

    if average_loss == 0:
        return 100.0

    rs = average_gain / average_loss

    rsi = 100 - (100 / (1 + rs))

    return round(rsi, 2)

def exponential_moving_average(rows, coin, period):
    if len(rows) < period:
        raise ValueError("Not enough price history")

    prices = [row[coin] for row in rows]

    multiplier = 2 / (period + 1)

    ema = sum(prices[:period]) / period

    for price in prices[period:]:
        ema = (price - ema) * multiplier + ema

    return round(ema, 2)

def macd(rows, coin):
    """
    Moving Average Convergence Divergence
    """

    if len(rows) < 35:
        raise ValueError("Not enough price history")

    prices = [row[coin] for row in rows]

    macd_values = []

    for i in range(26, len(prices)):
        subset = [{"price": p} for p in prices[:i + 1]]

        ema12 = exponential_moving_average(subset, "price", 12)
        ema26 = exponential_moving_average(subset, "price", 26)

        macd_values.append(ema12 - ema26)

    signal = sum(macd_values[-9:]) / 9

    current_macd = macd_values[-1]

    histogram = current_macd - signal

    return {
        "ema12": round(ema12, 2),
        "ema26": round(ema26, 2),
        "macd": round(current_macd, 2),
        "signal": round(signal, 2),
        "histogram": round(histogram, 2),
    }


def bollinger_bands(rows, coin, period=20, std_dev=2):
    """
    Calculates Bollinger Bands.

    Returns:
        middle
        upper
        lower
        bandwidth
        percent_b
    """

    if len(rows) < period:
        raise ValueError("Not enough price history")

    prices = [row[coin] for row in rows[-period:]]

    middle = sum(prices) / period

    variance = sum((price - middle) ** 2 for price in prices) / period
    standard_deviation = math.sqrt(variance)

    upper = middle + std_dev * standard_deviation
    lower = middle - std_dev * standard_deviation

    bandwidth = ((upper - lower) / middle) * 100 if middle else 0

    current_price = prices[-1]

    if upper == lower:
        percent_b = 0.5
    else:
        percent_b = (current_price - lower) / (upper - lower)

    return {
        "middle": round(middle, 2),
        "upper": round(upper, 2),
        "lower": round(lower, 2),
        "bandwidth": round(bandwidth, 2),
        "percent_b": round(percent_b, 2),
    }

