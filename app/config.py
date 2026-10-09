import os
from dotenv import load_dotenv
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
LLM_MODEL = os.getenv("MODEL_NAME","openai/gpt-oss-120b")

TEMPERATURE = float(os.getenv("TEMPERATURE", "0"))

TOP_K = 5

HF_TOKEN = os.getenv("HF_TOKEN")