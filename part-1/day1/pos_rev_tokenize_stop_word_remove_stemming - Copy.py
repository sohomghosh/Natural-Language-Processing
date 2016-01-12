from nltk.corpus import stopwords
english_stops = set(stopwords.words('english'))
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
filename="positive_reviews.txt"
filename2="positive_reviews_tokenized_with_stopwords-removed_and_stemming_done.txt";
f=open(filename,"r");
f2=open(filename2,"w");
while True:
	line=f.readline()
        if not line:
                break
        f2.write( str([stemmer.stem(i) for i in line.split() if i not in english_stops])+"\n")
f.close()
f2.close()
