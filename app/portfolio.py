from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings


class Portfolio:
    def __init__(self):
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        self.vectordb = Chroma(persist_directory="vectorstore", embedding_function=embeddings)

    def query_links(self, skill):
        results = self.vectordb.similarity_search(skill, k=2)
        return [doc.metadata['source'] for doc in results]