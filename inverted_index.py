from collections import defaultdict, Counter

class InvertedIndex:
    def __init__(self):
        self.index = defaultdict(list)
        self.vocabulary = set()
        self.doc_freq = defaultdict(int)
        self.term_freq = defaultdict(lambda: defaultdict(int))
        self.max_freq = {}

    # docs parameter is a list of multiple lists
    def create_index(self, docs:list):
        for doc_id, doc in enumerate(docs):
            term_counts = Counter(doc)
            most_frequent_word = max(term_counts, key=term_counts.get)
            self.max_freq[doc_id] = term_counts[most_frequent_word]

            for term, tf in sorted(term_counts.items()):
                self.index[term].append(doc_id)
                self.vocabulary.add(term)
                self.doc_freq[term] += 1
                self.term_freq[term][doc_id] = tf


"""
VISUALIZING THE GENERAL VALUES TO BE GENERATED
self.index = {
    'term1': [0, 2, 5],
    'term2': [1, 3, 4, 6],
    other terms and their document IDs
}
self.vocabulary = {'term1', 'term2', 'term3', 'term4', ...}
self.doc_freq = {
    'term1': 3,
    'term2': 4,
    other terms and their document frequencies
}
self.term_freq = {
    'term1': {0: 2, 2: 1, 5: 3},
    'term2': {1: 1, 3: 2, 4: 1, 6: 1},
    other terms and their term frequencies per document
}
"""