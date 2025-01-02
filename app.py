# import necessary modules and setup for FastAPI, LangGrapgh and LangChain

from fastapi import FastAPI  #FastApi framework for creating the web application
from pydantic import BaseModel # BaseModel for structured data models 
from typing import List # Used in RequestState model model to define a ist of messages
from langchain_community.tools.tavily_search import TavilySearchResults # Used for fetching external search results
import os # provides functionality to interact with the operating system
from langgraph.prebuilt import create_react_agent # Function to create React agent
from langchain_groq import ChatGroq # ChatGroq class for interacting with LLMs

groq_api_key = "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"
os.environ["TAVILY_API_KEY"] = "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"

MODEL_NAMES = [
    "llama3-70b-8192"
]

tool_tavily = TavilySearchResults(max_results=2)

tools = [tool_tavily,]

app = FastAPI(title="LangGraph AI Agent")

class RequestState(BaseModel):
    model_name: str
    system_prompt: str
    messages: List[str]

@app.post("/chat")
def chat_endpoint(request: RequestState):
    if request.model_name not in MODEL_NAMES:
        return {"error": "Invalid model name. Please select a valid model"}
    
    llm = ChatGroq(groq_api_key=groq_api_key, model_name = request.model_name)

    agent = create_react_agent(llm, tools = tools, state_modifier = request.system_prompt)

    state = {"messages": request.messages}

    result = agent.invoke(state)

    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)
