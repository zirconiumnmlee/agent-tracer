import json
import os
import time

class JSONRecorder:
    def __init__(self, output_dir):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def save(self, run):
        ts = time.strftime("%Y%m%d-%H%M%S")
        path = os.path.join(self.output_dir, f"{run['name']}_{ts}.json")

        with open(path, "w") as f:
            json.dump(run, f, indent=2, default=str)
