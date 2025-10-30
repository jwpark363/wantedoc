import os
# from langchain.document_loaders import TextLoader
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
# from langchain.vectorstores.pgvector import PGVector
from langchain_community.vectorstores.pgvector import PGVector

# Rule file to splits
def rule_to_splits(file_path:str, meta_name:str, chunk_size=500, chunk_overlap=50):
    print(f'****** loading file : {file_path}')
    loader = TextLoader(file_path)
    rule_docs = loader.load()
    print(f'****** spliting text')
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )
    splits = text_splitter.split_documents(rule_docs)
    print(f'****** add metadata : {meta_name}')
    for doc in splits:
        doc.metadata['name'] = meta_name
    return splits

# new Croma Vector Store
def splits_to_chromadb(splits,collection_name,persist_directory):
    print('****** creating croma vector store')
    Chroma.from_documents(
        documents=splits,
        embedding=OpenAIEmbeddings(),
        collection_name=collection_name,
        persist_directory=persist_directory
    )
    print('****** complete croma vector store')

def read_chromavector(collection_name,persist_directory):
    return Chroma(
        collection_name=collection_name,
        persist_directory=persist_directory,
        embedding_function=OpenAIEmbeddings(),
    )
    
## new PGVector Store
def splits_to_pgvector(splits,collection_name,connection_string):
    print('****** creating pgvector store')
    PGVector.from_documents(
        documents=splits,
        embedding=OpenAIEmbeddings(),
        collection_name=collection_name,
        connection_string=connection_string
    )
    print('****** complete pgvector store')

def read_pgvector(collection_name,connection_string):
    return PGVector(
        collection_name=collection_name,
        connection_string=connection_string,
        embedding_function=OpenAIEmbeddings(),
    )
