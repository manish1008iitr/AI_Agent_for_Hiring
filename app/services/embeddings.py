from langchain_huggingface import HuggingFaceEmbeddings 
from app.config import HF_TOKEN
_model = None 

def get_embedding_model(): 
    """ Lazily initialize and reuse the embedding model. """ 
    global _model 
    if _model is None: 
        _model = HuggingFaceEmbeddings( 
            model_name=( "sentence-transformers/all-MiniLM-L6-v2"),
            model_kwargs={"token": HF_TOKEN}  
            )
    return _model