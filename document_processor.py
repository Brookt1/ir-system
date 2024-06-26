import string
from stemmer import PorterStemmer

class DocumentProcessor:
    def __init__(self):
        self.stop_words = set([
            'the', 'and', 'is', 'in', 'it', 'of', 'to', 'a', 'an'
        ])
        self.stemmer = PorterStemmer()
    
    def preprocess(self, text):
        words = text.split()
        words = [self.stemmer.stem(word.lower().strip(string.punctuation)) for word in words if word.lower() not in self.stop_words]
        return words
