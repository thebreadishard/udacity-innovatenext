# Test script for DirectPromptAgent class

from workflow_agents.base_agents import DirectPromptAgent
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

prompt = "What is the Capital of France?"

direct_agent = DirectPromptAgent(openai_api_key)
direct_agent_response = direct_agent.respond(prompt)

# Print the response from the agent
print(direct_agent_response)

# The DirectPromptAgent passes the user prompt straight to the LLM with no system prompt,
# additional context, or retrieval step. The knowledge comes entirely from the LLM's own
# pre-trained weights (gpt-3.5-turbo general training data).
print("Knowledge source: gpt-3.5-turbo general pre-trained knowledge (no external context provided).")
