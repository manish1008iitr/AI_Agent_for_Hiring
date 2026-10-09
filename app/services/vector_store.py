from pathlib import Path 
from langchain_chroma import Chroma 
from app.services.embeddings import get_embedding_model

PROJECT_ROOT = Path(__file__).resolve().parents[2] 
VECTOR_DB_PATH = PROJECT_ROOT / "data" / "vectorstore"

COLLECTION_NAME = "resume_chunks"

def get_vector_store(): 
    """ Return the persistent Chroma vector store. """ 
    VECTOR_DB_PATH.mkdir( parents=True, exist_ok=True,)

    return Chroma( 
                collection_name= COLLECTION_NAME, 
                embedding_function = get_embedding_model(), 
                persist_directory=str(VECTOR_DB_PATH), 
            )

def add_resume_chunks(documents: list) -> list[str]: 
    """ Embed and store resume chunks. 
    Each document should contain candidate_id and section metadata. """ 
    if not documents: 
        return []

    vector_store = get_vector_store() 
    return vector_store.add_documents( 
            documents=documents 
        )

def search_resumes(query: str, k: int = 5, candidate_id: str | None = None, ) -> list:
    """ Retrieve semantically relevant resume chunks. 
    Optionally restrict results to one candidate. """

    vector_store = get_vector_store() 
    search_filter = None 
    if candidate_id: 
        search_filter = { "candidate_id": candidate_id }

    return vector_store.similarity_search( query=query, k=k, filter=search_filter, )




