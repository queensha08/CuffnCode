def run(v, c, p, r, status):
    return {
        "voltage": round(v, 2),
        "current": round(c, 2),
        "power": round(p, 2),
        "rms": round(r, 2),
        "status": status
    }