class EventBus:
    def __init__(self):
        self.queue = []

    def publish(self, data):
        self.queue.append(data)

    def subscribe(self):
        if self.queue:
            return self.queue.pop(0)
        return None