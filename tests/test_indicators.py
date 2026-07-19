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

