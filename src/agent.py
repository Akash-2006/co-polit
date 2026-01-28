from langchain_community.chat_models import ChatOllama
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.tools import tool
from langchain.memory import ConversationBufferMemory
from langchain.tools import HumanInputRun
import os


@tool
def search(query: str) -> str:
    """Search for information in the internet."""
    return f"Results: {query}"

def clear_terminal():
    # 'nt' is the name for Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # 'posix' is the name for Linux, macOS, etc.
    else:
        _ = os.system('clear')

class Agent:
    def __init__(self):
       llm = ChatOllama(model="llama3", base_url="http://localhost:11434",temperature=0)
       prompt = ChatPromptTemplate.from_messages([
        ("system", self.fetchPrompt()),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}")
    ])

       self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
       agent = create_react_agent(llm=llm, tools=[search],prompt=prompt)
       self.executor = AgentExecutor(
           agent=agent, 
           tools=[search],
           handle_parsing_errors=True,
           memory=self.memory,
           max_iterations=30,
           max_execution_time=300,
       )
       clear_terminal()

    def fetchPrompt(self):

        REACT_PROMPT = """
You are an intelligent assistant.

You have access to the following tools:

{tools}

Use the following format:

Thought: Do I need to use a tool? Yes/No
Action: The tool to use, must be one of [{tool_names}]
Action Input: The input to the tool
Observation: The result of the action

When you are ready to answer:

Thought: Do I need to use a tool? No
Final Answer: Your response to the user

New question:
{input}

{agent_scratchpad}
"""

        # Extend system message
        system_msg = """
        Important Rules:
        -If it is user details you must ask the user for the details and then answer the question.Instead of guessing the details and using the tools.
        - If the user's request is unclear, incomplete, ambiguous,
        or missing important details, you must ask a clear
        clarifying question before answering.
        - Do NOT guess.
        - Do NOT assume missing information.
        - Do NOT hallucinate.
        - If the user changes their mind, cancels, or says things like
        "never mind", "leave it", "stop", or similar,
        politely acknowledge and move on.
        - Keep responses concise and relevant.

    """

        return REACT_PROMPT+ system_msg


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
