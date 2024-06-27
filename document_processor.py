import string
from stemmer import PorterStemmer

class DocumentProcessor:
    def __init__(self):
        self.stop_words = set([
            'a', 'an', 'the', 'at', 'by', 'in', 'to', 'from', 'with', 'on', 'of', 'for',
            'about', 'over', 'under', 'through', 'and', 'but', 'as', 'because', 'or', 'nor',
            'if', 'while', 'when', 'i', 'you', 'he', 'she', 'it', 'we', 'they', 'me', 'him',
            'her', 'us', 'them', 'also', 'very', 'just', 'now', 'then', 'here', 'there',
            'one', 'two', 'three',
            'is', 'be', 'this', 'was', 'that', 'some', 'out', 'were', 'can', 'all', 'only',
            'more', 'one', 'over', 'there', 'their', 'up', 'so', 'no', 'when',
            'other', 'than', 'then', 'this', 'very', 'into', 'any', 'each', 'these',
            'those', 'both', 'few', 'most', 'such', 'nor', 'not', 'own', 'same', 'so',
            'than', 'that', 'the', 'their', 'then', 'there', 'these', 'they', 'this',
            'those', 'to', 'too', 'very', 'was', 'we', 'what', 'when', 'where', 'which',
            'who', 'will', 'with', 'would', 'you',
            'in', 'since', 'who', 'your', 'in', 'while', 'our', 'was', 'at', 'our',
            'here', 'are', 'is', 'for', 'their', 'are', 'so', 'may', 'of', 'their',
            'even', 'those', 'who', 'with', 'on', 'my', 'was', 'because', 'than',
            'we', 'had', 'for', 'at', 'how', 'much', 'those', 'had', 'our', 'that',
            'a', 'of', 'which', 'we', 'both', 'to', 'the', 'which', 'that', 'and',
            'as', 'well', 'as', 'my', 'are', 'by', 'it'
        ])
        self.stemmer = PorterStemmer()
    
    def preprocess(self, text)->list:
        words = text.split()
        # Convert each word to lowercase + Remove any leading or trailing punctuation characters +
        # stemming to the cleaned word using stemmer + add to words list stemmed version of the word if it is not found in the set of stop words
        words = [self.stemmer.stem(word.lower().strip(string.punctuation)) for word in words if word.lower() not in self.stop_words]
        return words
