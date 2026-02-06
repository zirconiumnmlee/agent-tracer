from agent_tracer import Tracer
import argparse
import time

def test_mvp():
    from agent_tracer.step import Step

    tracer = Tracer()

    def fake_llm(prompt):
        time.sleep(0.3)
        return "This is a fake answer."

    with tracer.run("simple-agent"):
        step = Step(step_type="llm", prompt="What is agent tracing?")
        try:
            output = fake_llm(step.prompt)
            step.finish(output=output, token_usage={"prompt": 5, "completion": 7})
        except Exception as e:
            step.finish(error=str(e))
        tracer.add_step(step)


def test_decorator():
    from agent_tracer.decorators import trace_llm

    tracer = Tracer()

    @trace_llm(tracer)
    def fake_llm(prompt):
        time.sleep(0.2)
        return f"Answer to: {prompt}"

    with tracer.run("decorated-agent"):
        fake_llm("What is agent tracing?")
        fake_llm("Why use decorators?")


parser = argparse.ArgumentParser(
    description="Agent Tracer 测试脚本",  # 脚本描述
    epilog="使用示例: python test.py --item mvp"  # 底部提示
)
parser.add_argument("--item", type=str, default="mvp")
args = parser.parse_args()

if __name__ == "__main__":
    if args.item == "mvp":
        test_mvp()
    elif args.item == "decorator":
        test_decorator()