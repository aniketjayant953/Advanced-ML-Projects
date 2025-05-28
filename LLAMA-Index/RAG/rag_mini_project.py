# Importing all the dependencies
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core import StorageContext, load_index_from_storage
from dotenv import load_dotenv 
import os

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')


class RAG:
    def __init__(self, file_path):
        self.file_path = file_path

    def output(self, questions):
        documents = SimpleDirectoryReader().load_data()
        index = VectorStoreIndex(documents, show_progress=True)
        # We are going to store the data in the local disk
        index.storage_context.persist(persist_dir='storage/indexex')
        storage_context = StorageContext.from_defaults(persist_dir='storage/indexes')
        index = load_index_from_storage(storage_context=storage_context)
        query_engine = index.as_query_engine()

        result = query_engine.query(questions)
        return result.response

obj = RAG(r'data')
print(obj.output('list down name of all the candidate'))