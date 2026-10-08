import os
from dotenv import load_dotenv
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
LLM_MODEL = os.getenv("MODEL_NAME","openai/gpt-oss-120b")

TEMPERATURE = float(os.getenv("TEMPERATURE", "0"))


# python -c "from app.config import LLM_MODEL, TEMPERATURE, GROQ_API_KEY; 
# print(LLM_MODEL); print(TEMPERATURE); print('API key loaded:', bool(GROQ_API_KEY))"
# Use the above CLI command to ensure that enviroment variables are loaded succesfully.