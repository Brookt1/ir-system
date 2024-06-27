
import os
from document_processor import DocumentProcessor
from tfidf_calculator import TfIdfCalculator
from inverted_index import InvertedIndex
from collections import defaultdict



def welcome_page():
    welcome_text = """
╔════════════════════════════════════════════════════╗
║                                                    ║
║               Welcome to IR System!                ║
║                                                    ║
║     An Information Retrieval System using          ║
║      Inverted Index and Vector Space Model         ║
║                                                    ║
║         Created by:   Biruk Tesfaye                ║
║                       Yabets Zekaryas              ║
║                       Elyas Damenu                 ║
║                       Mahlet Demeke                ║
╚════════════════════════════════════════════════════╝
"""
    print(welcome_text)

def get_query():
    print()
    query = input("Please enter your query: ")
    print()
    return query

welcome_page()
def main():
    
    corpus_dir = "corpus"
    documents = []
    doc_name = defaultdict(int)
    idx = 0
    for filename in os.listdir('corpus'):
        if filename.endswith('.txt'):
            with open(os.path.join(corpus_dir, filename), 'r', encoding='utf-8') as file:
                doc_name[idx] = filename[:len(filename) - 4] # Extracts the document name without the .txt extension.
                documents.append(file.read()) # Reads the entire content of the file and appends it to the documents list.
                idx += 1

    processor = DocumentProcessor()
    inverted_index = InvertedIndex()
    tfidf_calculator = TfIdfCalculator(inverted_index)

    preprocessed_docs = [processor.preprocess(doc) for doc in documents]

    inverted_index.create_index(preprocessed_docs)
    tfidf_docs = tfidf_calculator.compute_tfidf(preprocessed_docs)

    query = get_query()
    preprocessed_query = processor.preprocess(query)
    if not preprocessed_query:
        print("You cann't search a stop word!")
    else:
        print(preprocessed_query)
        results = tfidf_calculator.retrieve_documents(preprocessed_query, tfidf_docs)
        if len(results) == 0:
            print('There is no documents that contain your query')
        else:
            for idx, sim in results:
                print(f"{doc_name[idx]}: (Similarity: {sim:.4f})")
        print('-----------------------------------------------------')
    main()
main()