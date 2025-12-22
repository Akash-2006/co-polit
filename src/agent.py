from langchain_community.chat_models import ChatOllama
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from langchain_core.tools import tool
from langchain.memory import ConversationBufferMemory


@tool
def search(query: str) -> str:
    """Search for information."""
    return f"Results: {query}"


class Agent:
    def __init__(self):
       llm = ChatOllama(model="llama3", base_url="http://localhost:11434")
       prompt = hub.pull("hwchase17/react-chat")
       self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
       agent = create_react_agent(llm=llm, tools=[search],prompt=prompt)
       self.executor = AgentExecutor(agent=agent, tools=[search],handle_parsing_errors=True,memory=self.memory)

    def run(self, text):
        return self.executor.invoke({"input": text})["output"]
    
    def fetchMemory(self):
        return self.memory.chat_memory.messages


if __name__ == "__main__":
    agent = Agent()
    while True:
        prompt = input("Enter the query ")
        if prompt == "exit":
            break
        print(agent.run(prompt))
