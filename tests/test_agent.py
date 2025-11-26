from src.agent import agent

def test_agent_runs():
    result = agent.invoke({"input": "hello"})
    assert result["output"] is not None