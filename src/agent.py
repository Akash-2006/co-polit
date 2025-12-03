from langchain_ollama import OllamaLLM

class Agent:
    llm = OllamaLLM(model="llama3.2")

    def run(self,input):
        return self.llm.invoke(input)
        


if __name__ == "__main__":
    agent = Agent()
    print(agent.run("Hello LangGraph"))