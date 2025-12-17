from src.agent import Agent

def test_agent_runs():
    agent = Agent()
    assert agent.run("hii") is not None

def test_agent_memory():
    agent = Agent()
    assert len(agent.fetchMemory()) is 0
    agent.run("hii")
    assert len(agent.fetchMemory()) is not 1