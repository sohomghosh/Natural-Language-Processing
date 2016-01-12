from nltk.corpus import stopwords
english_stops = set(stopwords.words('english'))
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
filename="whole_review.txt" #replace input_file by your own file name
filename2="new_intermidiate_tokenized_with_stopwords-removed_and_stemming_done.txt"; #this is the intermediate file
f=open(filename,"r");
f2=open(filename2,"w");
while True:
	line=f.readline()
        if not line:
            break
        _token=[stemmer.stem(i) for i in line.split() if i not in english_stops]
        #print(_token)
        i=0
        while True:
            if(i==len(_token)):
                break
            f2.write( str(_token[i])+" ")
            i=i+1
        f2.write("\n")
f.close()
f2.close()
