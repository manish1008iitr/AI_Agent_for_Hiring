from langchain_groq import ChatGroq
from app.config import GROQ_API_KEY, LLM_MODEL, TEMPERATURE

def get_llm() -> ChatGroq:
    if not GROQ_API_KEY or not LLM_MODEL or TEMPERATURE:
        raise ValueError(
            "GROQ_API_KEY is not configured. "
            "Please check your .env file."
        )

    llm = ChatGroq(
        model= LLM_MODEL,
        temperature= TEMPERATURE,
        api_key= GROQ_API_KEY,
    )

    return llm

