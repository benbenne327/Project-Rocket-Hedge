def moving_average(rows, coin, period=10):
 recent = rows[-min(period, len(rows)):]
 return sum(r[coin] for r in recent) / len(recent)
