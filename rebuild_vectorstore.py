from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import CSVLoader

print("Loading CSV...")
loader = CSVLoader(file_path='my_portfolio.csv', source_column="Links")
data = loader.load()
print(f"Loaded {len(data)} portfolio items")

print("Creating embeddings...")
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

print("Creating vectorstore...")
vectordb = Chroma.from_documents(
    documents=data,
    embedding=embeddings,
    persist_directory="vectorstore"
)
vectordb.persist()
print("Done! vectorstore folder created")