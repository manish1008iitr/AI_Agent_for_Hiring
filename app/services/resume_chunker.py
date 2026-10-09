from langchain_experimental.text_splitter import SemanticChunker 
from langchain_huggingface import HuggingFaceEmbeddings

from app.services.resume_schema import ProcessedResume
from app.config import HF_TOKEN

# Initialize the embedding model once. 
_embeddings = HuggingFaceEmbeddings( 
    model_name="sentence-transformers/all-MiniLM-L6-v2", 
    model_kwargs={"token": HF_TOKEN}  
    )

# Initialize the semantic splitter once. 
_semantic_splitter = SemanticChunker( embeddings=_embeddings, breakpoint_threshold_type="percentile", )


def chunk_resume(resume: ProcessedResume): 
    """ Split a processed resume into semantically meaningful chunks while 
    preserving candidate and section metadata. 
    Returns: A list of LangChain Document objects. """ 
    documents = []

    for section in resume.sections:
        content = section.content.strip()

        if not content: 
            continue

        section_documents = _semantic_splitter.create_documents( 
            texts=[content], 
            metadatas=[ 
                { "candidate_id": resume.candidate_id, 
                "file_name": resume.file_name, 
                "section": section.section_name, 
                } 
            ], 
        )

        documents.extend(section_documents)

    return documents



