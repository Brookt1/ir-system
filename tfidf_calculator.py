import math
from collections import defaultdict, Counter

class TfIdfCalculator:
    def __init__(self, inverted_index):
        self.inverted_index = inverted_index
        self.idf = defaultdict(float)
    
    def compute_idf(self, n_docs:int):
        for term, df in self.inverted_index.doc_freq.items():
            self.idf[term] = math.log(n_docs / ( df))
    
    def compute_tfidf(self, docs:list)->list:
        tfidf_docs = []
        self.compute_idf(len(docs))
        
        for doc_id, doc in enumerate(docs):
            tfidf = {}
            # for each term inside each document find the weight(tf*idf)
            for term in doc:
                tf = self.inverted_index.term_freq[term][doc_id] / self.inverted_index.max_freq[doc_id]
                tfidf[term] = tf * self.idf[term]
            tfidf_docs.append(tfidf)
        
        return tfidf_docs
    
    def retrieve_documents(self, query, tfidf_docs):
        query_tf = Counter(query) # returns a dictionary that contains distinct query terms with their frequencies
        query_tfidf = {}
        for term, tf_val in query_tf.items():
            query_tfidf[term] = tf_val / query_tf[max(query_tf, key=query_tf.get)] * self.idf.get(term, 0)
        
        similarities = []
        for idx, doc_tfidf in enumerate(tfidf_docs):
            sim = self.cosine_similarity(query_tfidf, doc_tfidf)
            similarities.append((idx, sim))
        
        similarities.sort(key=lambda x: x[1], reverse=True)
        filtered = []
        for idx, sim in similarities:
            if sim > 0:
                filtered.append((idx, sim))
        return filtered
    
    def cosine_similarity(self, vec1, vec2):
        dot_product = sum(vec1[term] * vec2.get(term, 0) for term in vec1)
        norm1 = math.sqrt(sum(val ** 2 for val in vec1.values()))
        norm2 = math.sqrt(sum(val ** 2 for val in vec2.values()))
        if norm1 == 0 or norm2 == 0:
            return 0.0
        return dot_product / (norm1 * norm2)
