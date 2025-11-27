# Co-Polit

A project to replicate GitHub Copilot features using open-source LLMs and LangGraph.

## Overview

Co-Polit is an experimental AI coding assistant that aims to replicate core features of GitHub Copilot using locally-running language models via Ollama and the LangGraph framework. This project demonstrates how to build an intelligent coding agent that can understand and respond to programming-related queries.

## Features

- 🤖 **Local LLM Integration**: Leverages Ollama with Llama 3.2 for on-device AI inference
- 🔄 **Agent-Based Architecture**: Built with LangGraph for stateful, graph-based agent workflows
- 🔒 **Privacy-First**: All processing happens locally without sending code to external APIs
- 🧪 **Test Coverage**: Includes pytest-based testing infrastructure
- 🎨 **Code Quality Tools**: Integrated with Black, isort, and flake8 for consistent code formatting

## Architecture

The project uses a simple yet extensible agent architecture:

```
┌─────────────┐
│    Input    │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Agent Step  │──► LangGraph State Management
│  (LLM Call) │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Output    │
└─────────────┘
```

## Prerequisites

- Python 3.8+
- [Ollama](https://ollama.ai/) installed and running
- Llama 3.2 model pulled in Ollama

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Akash-2006/co-polit.git
   cd co-polit
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv env
   source env/bin/activate  # On macOS/Linux
   # or
   env\Scripts\activate  # On Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up pre-commit hooks** (optional):
   ```bash
   pre-commit install
   ```

5. **Ensure Ollama is running with Llama 3.2**:
   ```bash
   ollama pull llama3.2
   ollama serve
   ```

## Usage

### Basic Agent Interaction

Run the main agent:

```bash
python src/agent.py
```

This will initialize the LangGraph agent and send a test query to the LLM.

### Custom Queries

Modify the input in `src/agent.py`:

```python
result = agent.invoke({"input": "Your custom prompt here"})
print(result)
```

## Project Structure

```
co-polit/
├── README.md              # This file
├── requirements.txt       # Python dependencies
├── src/
│   └── agent.py          # Main agent implementation
├── tests/
│   └── agent.py          # Test suite
└── env/                  # Virtual environment (gitignored)
```

## Development

### Running Tests

```bash
pytest
```

### Code Coverage

```bash
coverage run -m pytest
coverage report
```

### Code Formatting

Format code with Black:
```bash
black src/ tests/
```

Sort imports with isort:
```bash
isort src/ tests/
```

Lint with flake8:
```bash
flake8 src/ tests/
```

## Roadmap

Future enhancements planned for Co-Polit:

- [ ] Code completion suggestions
- [ ] Multi-file context awareness
- [ ] Function and docstring generation
- [ ] Code review and refactoring suggestions
- [ ] Integration with VS Code extension
- [ ] Support for multiple LLM backends
- [ ] RAG-based documentation lookup
- [ ] Unit test generation
- [ ] Bug detection and fixing

## Technologies Used

- **[LangGraph](https://github.com/langchain-ai/langgraph)**: Framework for building stateful, multi-agent applications
- **[LangChain](https://github.com/langchain-ai/langchain)**: Orchestration layer for LLM applications
- **[Ollama](https://ollama.ai/)**: Local LLM runtime
- **[Llama 3.2](https://ollama.ai/library/llama3.2)**: Meta's open-source language model
- **pytest**: Testing framework
- **Black/isort/flake8**: Code quality tools

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- Inspired by GitHub Copilot
- Built with the LangChain and LangGraph ecosystem
- Powered by Ollama and Llama 3.2

## Contact

Project Link: [https://github.com/Akash-2006/co-polit](https://github.com/Akash-2006/co-polit)

---

**Note**: This is an experimental project for educational purposes. It is not affiliated with or endorsed by GitHub or Microsoft.
