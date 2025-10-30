import os
from dotenv import load_dotenv
from lib.rag.util import rule_to_splits, splits_to_chromadb, read_chromavector, read_pgvector
from agent.rule_rag import init_chromavectorstore, init_pgtorstore

load_dotenv()
RULE_DIR = os.getenv('RULE_DIR')
COLLECTION_NAME = os.getenv('COLLECTION_NAME')
PERSIST_DIRECTORY = os.getenv('PERSIST_DIRECTORY')
CONNECTION_STRING = os.getenv('RAG_DB_URL')
RAG_INITIALIZATION_REQUIRED = os.getenv('RAG_INITIALIZATION_REQUIRED')
RAG_CROMA_VECTOR = os.getenv('RAG_CROMA_VECTOR')
RAG_PG_VECTOR = os.getenv('RAG_PG_VECTOR')

if __name__ == '__main__':
    print('*** RAG Initializer start ***')
    print(f'RAG_INITIALIZATION_REQUIRED : {RAG_INITIALIZATION_REQUIRED}')
    print(f'RAG_CROMA_VECTOR : {RAG_CROMA_VECTOR}')
    print(f'RAG_PG_VECTOR : {RAG_PG_VECTOR}')

    if RAG_INITIALIZATION_REQUIRED == 'true':
        # croma vectore 초기화
        if RAG_CROMA_VECTOR == 'true':
            print('RAG_CROMA_VECTOR')
            init_chromavectorstore()
        # pgvector 초기화
        if RAG_PG_VECTOR == 'true':
            print('RAG_PG_VECTOR')
            init_pgtorstore()