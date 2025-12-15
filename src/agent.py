from langchain_community.chat_models import ChatOllama
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from langchain_core.tools import tool


@tool
def search(query: str) -> str:
    """Search for information."""
    return f"Results: {query}"


class Agent:
    def __init__(self):
       llm = ChatOllama(model="llama3", base_url="http://localhost:11434")
       prompt = hub.pull("hwchase17/react")
       agent = create_react_agent(llm=llm, tools=[search],prompt=prompt)
       self.executor = AgentExecutor(agent=agent, tools=[search],verbose=True,handle_parsing_errors=True)

    def run(self, text):
        return self.executor.invoke({"input": text})


if __name__ == "__main__":
    agent = Agent()
    print(agent.run("what are the tools that are available?"))
