from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.embedder.openai import OpenAIEmbedder
from phi.knowledge.pdf import PDFUrlKnowledgeBase
from phi.vectordb.lancedb import LanceDb, SearchType

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

def compile_knowledge_base(urls):
    knowledge_base = PDFUrlKnowledgeBase(
    urls=urls,
    vector_db=LanceDb(
        table_name="llm",
        uri="tmp/lancedb",
        search_type=SearchType.vector,
        embedder=OpenAIEmbedder(model="text-embedding-3-small"),
        ),
    )
    
    knowledge_base.load()

    return knowledge_base