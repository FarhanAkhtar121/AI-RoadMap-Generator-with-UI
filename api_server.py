from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from conversation_agent import RoadmapConversationAgent
from dynamic_llm_conversation_agent import DynamicLLMConversationAgent
import os
from fastapi.staticfiles import StaticFiles

app = FastAPI()
# agent = RoadmapConversationAgent()  # Single global agent
openai_api_key = os.getenv("OPENAI_API_KEY")  # Make sure your key is in your .env or environment

agent = DynamicLLMConversationAgent(openai_api_key=openai_api_key)

# Allow CORS for local frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, restrict this!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory session store (for demo; use Redis or DB for production)


class ConversationInput(BaseModel):
    user_input: str

@app.post("/api/conversation")
async def conversation(input: ConversationInput):
    result = agent.handle_user_input(input.user_input)
    app.mount("/output", StaticFiles(directory="output"), name="output")
    return result