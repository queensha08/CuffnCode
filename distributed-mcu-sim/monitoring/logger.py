import csv
import os
from datetime import datetime

LOG_FILE = "logs/system_log.csv"

def init():
    os.makedirs("logs", exist_ok=True)
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["time","v","c","p","r","status"])

def log(v,c,p,r,status):
    init()
    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now().strftime("%H:%M:%S"),
            v,c,p,r,status
        ])