import time
from contextlib import contextmanager
from .step import Step
from .recorder import JSONRecorder

class Tracer:
    def __init__(self, project="default", output_dir="runs"):
        self.project = project
        self.recorder = JSONRecorder(output_dir)
        self.current_run = None

    @contextmanager
    def run(self, name):
        self.current_run = {
            "name": name,
            "start_time": time.time(),
            "steps": []
        }
        try:
            yield
        finally:
            self.current_run["end_time"] = time.time()
            self.recorder.save(self.current_run)
            self.current_run = None

    def add_step(self, step: Step):
        self.current_run["steps"].append(step)
