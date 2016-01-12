import nltk
from nltk.corpus import stopwords
s = open("negative_reviews_sam.txt").read()
tokens = nltk.word_tokenize(s)
def cleanupDoc(s):
    stopset = set(stopwords.words('english'))
    tokens = nltk.word_tokenize(s)
    cleanup = [token.lower()for token in tokens.lower() not in stopset and  len(token)>2]
    return cleanup
cleanupDoc(s)
