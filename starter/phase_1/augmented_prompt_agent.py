from workflow_agents.base_agents import AugmentedPromptAgent
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve OpenAI API key from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")

prompt = "What is the capital of France?"
persona = "You are a college professor; your answers always start with: 'Dear students,'"

augmented_agent = AugmentedPromptAgent(openai_api_key, persona)

augmented_agent_response = augmented_agent.respond(prompt)

# Print the agent's response
print(augmented_agent_response)

# Knowledge source: the agent relies on gpt-3.5-turbo's general pre-trained knowledge to
# answer the factual question — no external documents or retrieval are involved.
#
# Effect of the persona: the system prompt forces the model to role-play as a college
# professor, so the response is framed in an academic tone and always opens with
# "Dear students," — the same underlying fact is delivered in a style shaped entirely
# by the persona rather than the model's default conversational style.
print("\n--- Analysis ---")
print("Knowledge source: gpt-3.5-turbo general pre-trained knowledge (no external documents or retrieval).")
print("Persona impact: The system prompt instructs the model to act as a college professor, "
      "causing the response to adopt an academic tone and always begin with 'Dear students,' "
      "demonstrating how persona augmentation shapes style without changing the underlying factual content.")
