def process(data):
    v, c, p, r, status = data
    label = "FAULT" if status == "ANOMALY" else "NORMAL"
    return v, c, p, r, label