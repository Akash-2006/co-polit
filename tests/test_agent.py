from src.agent import Agent

def test_agent_runs():
    agent = Agent()
    assert agent.run("hii") is not None