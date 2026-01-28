import math
from langchain_community.chat_models import ChatOllama
from langchain.agents import Tool, create_react_agent, AgentExecutor
from langchain import hub
from langchain_core.tools import tool
from langchain.memory import ConversationBufferMemory


@tool
def calculator(expression: str) -> str:
    """
    Evaluate a mathematical expression.
    Example: "2 + 3 * 4"
    """
    try:
        result = eval(expression, {"__builtins__": {}}, math.__dict__)
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"


@tool
def search_web(url: str) -> str:
    """
    Search the web for information.
    Example: "https://www.google.com"
    """
    return f"Results: {url}"


class Agent:
    def __init__(self):
       llm = ChatOllama(model="llama3", base_url="http://localhost:11434",temperature=0.0)
       prompt = hub.pull("hwchase17/react-chat")
       self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
       agent = create_react_agent(llm=llm, tools=[calculator,search_web],prompt=prompt)
       self.executor = AgentExecutor(agent=agent, tools=[calculator,search_web],handle_parsing_errors=True,memory=self.memory,verbose=True)

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
