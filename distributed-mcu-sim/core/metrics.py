import time

class Metrics:
    def __init__(self):
        self.start = None
        self.times = []

    def start_timer(self):
        self.start = time.time()

    def end_timer(self):
        if self.start:
            self.times.append(time.time() - self.start)

    def avg_latency(self):
        return sum(self.times)/len(self.times) if self.times else 0