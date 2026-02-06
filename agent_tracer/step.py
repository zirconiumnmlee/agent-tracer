import time
import uuid

class Step:
    def __init__(self, step_type, input=None, prompt=None):
        self.step_id = str(uuid.uuid4())
        self.type = step_type
        self.input = input
        self.prompt = prompt
        self.output = None
        self.error = None
        self.start_time = time.time()
        self.end_time = None
        self.token_usage = None
        self.cost_usd = 0.0

    def finish(self, output=None, error=None, token_usage=None, cost_usd=0.0):
        self.end_time = time.time()
        self.output = output
        self.error = error
        self.token_usage = token_usage
        self.cost_usd = cost_usd

    @property
    def latency_ms(self):
        if self.end_time is None:
            return None
        return int((self.end_time - self.start_time) * 1000)
