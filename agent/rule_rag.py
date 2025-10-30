import os
from dotenv import load_dotenv
from lib.rag.util import rule_to_splits, splits_to_chromadb, splits_to_pgvector

load_dotenv()

## 설정 파일 처리?
RULE_DIR = os.getenv('RULE_DIR')
COLLECTION_NAME = os.getenv('COLLECTION_NAME')
PERSIST_DIRECTORY = os.getenv('PERSIST_DIRECTORY')
CONNECTION_STRING = os.getenv('RAG_DB_URL')

## initialize vectorstore
def init_chromavectorstore():
    print('--- 1. initialize vector store ---')
    print(f'--- rule dir : {RULE_DIR}')
    spliters = []
    for rule_file in os.listdir(RULE_DIR):
        rule_name, _ = rule_file.split('_')
        print(f'--- split file : {RULE_DIR}/{rule_file} / {rule_name}')
        spliters.extend(rule_to_splits(f'{RULE_DIR}/{rule_file}', rule_name))
    print(f'--- creating croma vector store')
    print(f'--- collection name : {COLLECTION_NAME}')
    print(f'--- persist directory : {PERSIST_DIRECTORY}')
    splits_to_chromadb(
        splits=spliters,
        collection_name=COLLECTION_NAME,
        persist_directory=PERSIST_DIRECTORY
    )
    print('--- 1. completed ---')
    
## initialize vectorstore
def init_pgtorstore():
    print('--- 1. initialize vector store ---')
    print(f'--- rule dir : {RULE_DIR}')
    spliters = []
    for rule_file in os.listdir(RULE_DIR):
        rule_name, _ = rule_file.split('_')
        print(f'--- split file : {RULE_DIR}/{rule_file} / {rule_name}')
        spliters.extend(rule_to_splits(f'{RULE_DIR}/{rule_file}', rule_name))
    print(f'--- creating croma vector store')
    print(f'--- collection name : {COLLECTION_NAME}')
    print(f'--- persist directory : {PERSIST_DIRECTORY}')
    splits_to_pgvector(
        splits=spliters,
        collection_name=COLLECTION_NAME,
        connection_string=CONNECTION_STRING
    )
    print('--- 1. completed ---')