from unittest.mock import patch

from src.agent import Agent, calculator, search_web


# --- Agent tests ---


def test_agent_runs():
    agent = Agent()
    assert agent.run("hii") is not None


def test_agent_memory_starts_empty():
    agent = Agent()
    assert len(agent.fetchMemory()) == 0


def test_agent_memory_after_run():
    agent = Agent()
    agent.run("hii")
    assert len(agent.fetchMemory()) > 0


# --- Calculator tool tests ---


@patch("src.agent.input", return_value="yes")
def test_calculator_evaluates_expression(mock_input):
    result = calculator.invoke({"expression": "2 + 3 * 4"})
    assert result == "14"


@patch("src.agent.input", return_value="yes")
def test_calculator_handles_simple_math(mock_input):
    result = calculator.invoke({"expression": "10 - 3"})
    assert result == "7"


@patch("src.agent.input", return_value="no")
def test_calculator_denied_by_user(mock_input):
    result = calculator.invoke({"expression": "2 + 2"})
    assert result == "Tool use denied by user."


@patch("src.agent.input", return_value="yes")
def test_calculator_invalid_expression_returns_error(mock_input):
    result = calculator.invoke({"expression": "not valid math"})
    assert result.startswith("Error:")


# --- Search web tool tests ---


@patch("src.agent.input", return_value="yes")
def test_search_web_returns_results_when_allowed(mock_input):
    result = search_web.invoke({"url": "https://example.com"})
    assert result == "Results: https://example.com"


@patch("src.agent.input", return_value="no")
def test_search_web_denied_by_user(mock_input):
    result = search_web.invoke({"url": "https://example.com"})
    assert result == "Tool use denied by user."