from langchain_ollama import OllamaLLM
from langgraph.graph import StateGraph, END

llm = OllamaLLM(model="llama3.2")

def agent_step(state):
    response = llm.invoke(state["input"])
    return {"output": response}

graph = StateGraph(dict)
graph.add_node("agent", agent_step)
graph.set_entry_point("agent")
graph.add_edge("agent", END)

agent = graph.compile()

print(agent.invoke({"input": "Hello LangGraph"}))