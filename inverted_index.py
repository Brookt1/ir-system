from collections import defaultdict, Counter

class InvertedIndex:
    def __init__(self):
        self.index = defaultdict(list)
        self.vocabulary = set()
        self.doc_freq = defaultdict(int)
        self.term_freq = defaultdict(lambda: defaultdict(int)) 
    
    def create_index(self, docs):
        for doc_id, doc in enumerate(docs):
            term_counts = Counter(doc) 
            for term, tf in term_counts.items():
                self.index[term].append(doc_id)
                self.vocabulary.add(term)
                self.doc_freq[term] += 1
                self.term_freq[term][doc_id] = tf 

