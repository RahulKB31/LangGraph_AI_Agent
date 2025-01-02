# LangGraph AI Agent

LangGraph AI Agent is a FastAPI-based web application that integrates LangGraph, LangChain, and Groq LLMs to create a powerful AI agent capable of interacting with users and fetching external search results using the Tavily API. The project also includes a Streamlit UI for a seamless user experience.

## Features
- **FastAPI Backend**: A high-performance backend for handling chat requests.
- **LangGraph Integration**: Utilizes LangGraph to create a ReAct agent for decision-making.
- **Tavily Search**: Fetches external search results to enhance the agent's responses.
- **Groq LLMs**: Supports multiple Groq models (`llama3-70b-8192` and `mixtral-8x7b-32768`) for generating responses.
- **Streamlit UI**: A user-friendly interface for interacting with the AI agent.

![Screenshot 2025-01-02 222353.jpg(https://github.com/RahulKB31/LangGraph_AI_Agent/blob/master/Screenshot%202025-01-02%20222353.jpg)


## Prerequisites
Before running the project, ensure you have the following:

- Python 3.8 or higher
- A Groq API key (sign up at [Groq](https://groq.com))
- A Tavily API key (sign up at [Tavily](https://tavily.com))

## Installation

### Clone the repository:

```bash
git clone https://github.com/yourusername/langgraph-ai-agent.git
cd langgraph-ai-agent
```

### Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Set up environment variables:

Create a `.env` file in the root directory and add your API keys:

```plaintext
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

## Running the Application

### Start the FastAPI Backend

Run the FastAPI server using the following command:

```bash
uvicorn main:app --reload
```

The backend will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).

### Start the Streamlit UI

In a separate terminal, start the Streamlit UI:

```bash
streamlit run main.py
```

The UI will be accessible at [http://localhost:8501](http://localhost:8501).

## Usage

1. **Define Your AI Agent**: Enter a system prompt in the text area to define the behavior of the AI agent.
2. **Select Model**: Choose a Groq model from the dropdown list (`llama3-70b-8192` or `mixtral-8x7b-32768`).
3. **Enter Your Message**: Type your message in the text area.
4. **Submit**: Click the "Submit" button to send your message to the AI agent. The agent will process your message and return a response, which will be displayed in the UI.

## API Endpoint

The FastAPI backend exposes a `/chat` endpoint that accepts POST requests with the following JSON payload:

### Request:

```json
{
  "model_name": "llama3-70b-8192",
  "system_prompt": "You are a helpful assistant.",
  "messages": ["Hello, how are you?"]
}
```

### Response:

```json
{
  "messages": [
    {
      "type": "ai",
      "content": "I'm doing well, thank you! How can I assist you today?"
    }
  ]
}
```

## Project Structure

```plaintext
langgraph-ai-agent/
├── main.py               # FastAPI backend and Streamlit UI
├── requirements.txt      # List of dependencies
├── .env                  # Environment variables for API keys
├── README.md             # Project documentation
```

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes.
4. Submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- **Groq** for providing powerful LLMs.
- **Tavily** for enabling external search capabilities.
- **LangChain** and **LangGraph** for their robust frameworks for building AI agents.

Enjoy building and interacting with your LangGraph AI Agent! 🚀
