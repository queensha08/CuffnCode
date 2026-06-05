def process(data):
    v, c, p, r = data
    status = "ANOMALY" if p > 260 else "NORMAL"
    return v, c, p, r, status