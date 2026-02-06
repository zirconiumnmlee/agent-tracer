import functools
from .step import Step

def trace_step(tracer, step_type="generic"):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            step = Step(
                step_type=step_type,
                input={"args": args, "kwargs": kwargs}
            )

            try:
                result = func(*args, **kwargs)
                step.finish(output=result)
                return result
            except Exception as e:
                step.finish(error=str(e))
                raise
            finally:
                tracer.add_step(step)

        return wrapper
    return decorator

def trace_llm(tracer):
    return trace_step(tracer, step_type="llm")
