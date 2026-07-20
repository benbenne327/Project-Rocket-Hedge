def build_signal(analysis, rsi, macd_data, bollinger):
    """
    Combines several technical indicators into a transparent score.

    Positive scores indicate bullish evidence.
    Negative scores indicate bearish evidence.

    This is a heuristic analysis tool, not a guarantee of market direction.
    """

    score = 0
    reasons = []

    # Moving-average trend
    trend = analysis["trend"]

    if trend == "UP":
        score += 2
        reasons.append("Short moving average is above the long moving average")
    elif trend == "DOWN":
        score -= 2
        reasons.append("Short moving average is below the long moving average")
    else:
        reasons.append("Moving averages indicate a sideways market")

    # RSI
    if rsi <= 30:
        score += 2
        reasons.append("RSI indicates oversold conditions")
    elif rsi >= 70:
        score -= 2
        reasons.append("RSI indicates overbought conditions")
    elif 45 <= rsi <= 55:
        reasons.append("RSI is neutral")
    elif rsi < 45:
        score += 1
        reasons.append("RSI shows mild bearish pressure with possible value")
    else:
        score -= 1
        reasons.append("RSI shows mild bullish pressure approaching overbought")

    # MACD
    if macd_data is not None:
        histogram = macd_data["histogram"]

        if histogram > 0:
            score += 2
            reasons.append("MACD is above its signal line")
        elif histogram < 0:
            score -= 2
            reasons.append("MACD is below its signal line")
        else:
            reasons.append("MACD is neutral")

    # Bollinger Bands
    if bollinger is not None:
        percent_b = bollinger["percent_b"]

        if percent_b <= 0:
            score += 2
            reasons.append("Price is at or below the lower Bollinger Band")
        elif percent_b >= 1:
            score -= 2
            reasons.append("Price is at or above the upper Bollinger Band")
        elif percent_b <= 0.2:
            score += 1
            reasons.append("Price is near the lower Bollinger Band")
        elif percent_b >= 0.8:
            score -= 1
            reasons.append("Price is near the upper Bollinger Band")
        else:
            reasons.append("Price is inside the central Bollinger range")

    # Recommendation
    if score >= 4:
        recommendation = "STRONG BUY"
    elif score >= 2:
        recommendation = "BUY"
    elif score <= -4:
        recommendation = "STRONG SELL"
    elif score <= -2:
        recommendation = "SELL"
    else:
        recommendation = "HOLD"

    maximum_score = 8
    confidence = min(round(abs(score) / maximum_score * 100), 100)

    return {
        "score": score,
        "recommendation": recommendation,
        "confidence": confidence,
        "reasons": reasons,
    }
