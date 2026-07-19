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

