from agent_tracer import Tracer
from agent_tracer.step import Step
import time

def fake_llm(prompt):
    time.sleep(0.3)
    return "This is a fake answer."

tracer = Tracer(project="demo")

with tracer.run("simple-agent"):
    step = Step(step_type="llm", prompt="What is agent tracing?")
    try:
        output = fake_llm(step.prompt)
        step.finish(output=output, token_usage={"prompt": 5, "completion": 7})
    except Exception as e:
        step.finish(error=str(e))
    tracer.add_step(step)