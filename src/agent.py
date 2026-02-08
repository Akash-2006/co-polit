import math
from langchain_community.chat_models import ChatOllama
from langchain.agents import Tool, create_react_agent, AgentExecutor
from langchain import hub
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.tools import tool
from langchain.memory import ConversationBufferMemory
from langchain.tools import HumanInputRun
import os


def human_permission(tool) -> str:
    """
    Ask the user for permission to use the tool.
    Example: "calculator"
    """
    return input(f"\n Do you want to use the {tool.name} tool? (yes/no): ") == "yes"

@tool
def calculator(expression: str) -> str:
    """
    Evaluate a mathematical expression.
    Example: "2 + 3 * 4"
    """
    try:
        if not human_permission(calculator):
            return "Tool use denied by user."
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
    if not human_permission(search_web):
            return "Tool use denied by user."
    return f"Results: {url}"

def clear_terminal():
    # 'nt' is the name for Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # 'posix' is the name for Linux, macOS, etc.
    else:
        _ = os.system('clear')

class Agent:
    def __init__(self):
       llm = ChatOllama(model="llama3", base_url="http://localhost:11434",temperature=0.0)
       prompt = hub.pull("hwchase17/react-chat")
       self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
       agent = create_react_agent(llm=llm, tools=[calculator,search_web],prompt=prompt)
       self.executor = AgentExecutor(agent=agent, tools=[calculator,search_web],handle_parsing_errors=True,memory=self.memory,verbose=True)

    def run(self, text):
        result = self.executor.invoke({"input": text})
        return result["output"]
    
    def fetchMemory(self):
        return self.memory.chat_memory.messages


if __name__ == "__main__":
    agent = Agent()
    while True:
        prompt = input("Enter the query ")
        if prompt == "exit":
            break
        print(agent.run(prompt))
