from app.indicators import moving_average

rows = [
    {"bitcoin": 10.0},
    {"bitcoin": 20.0},
    {"bitcoin": 30.0},
    {"bitcoin": 40.0},
    {"bitcoin": 50.0},
]

result = moving_average(rows, "bitcoin", 3)
expected = 40.0

assert result == expected, f"Expected {expected}, got {result}"
print("✅ Moving-average test passed.")
