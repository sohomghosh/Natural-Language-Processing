#WRITTEN BY SOHOM GHOSH (sohom1ghosh@gmail.com)
import nltk
filename="input_whole_review_test2.txt"#replace whole_review_test2.txt by your input filename.txt
filename1="whole_review_with_adv_adj_only_intermediate.txt"
fp=open(filename,'r')
fp1=open(filename1,'w')
while True:
    line=fp.readline()
    if not line:
        break
    token=line.strip().split(' ')
    pos_tags = nltk.pos_tag(token)
    fp1.write( str(nltk.ne_chunk(pos_tags, binary=True)))
fp.close()
fp1.close()
import nltk
filename="whole_review_with_adv_adj_only_intermediate.txt"
filename1="whole_review_with_adv_adj_only_intermediate1.txt"
fp=open(filename,'r')
fp1=open(filename1,'w')
while True:
    line=fp.readline()
    if not line:
        break
    token=line.strip().split(' ')
    fp1.write(str( token[0])+"\n")
fp.close()
fp1.close()
import nltk
filename="whole_review_with_adv_adj_only_intermediate1.txt"
filename1="whole_review_with_adv_adj_only_intermediate2.txt"
fp=open(filename,'r')
fp1=open(filename1,'w')
while True:
    line=fp.readline()
    if not line:
        break
    token=line.strip().split('/')
    if len(token)>1:
        fp1.write(str( token[0])+" "+token[1]+"\n")
fp.close()
fp1.close()
import nltk
filename="whole_review_with_adv_adj_only_intermediate2.txt"
filename1="whole_review_with_adv_adj_only_final.txt"
fp=open(filename,'r')
fp1=open(filename1,'w')
while True:
    line=fp.readline()
    if not line:
        break
    token=line.strip().split(' ')
    if len(token)>1:
        if token[1]=='RBS' or token[1]=='RBR' or token[1]=='RB' or token[1]=='JJS' or token[1]=='JJR' or token[1]=='JJ':
            fp1.write(token[0]+"\n")
fp.close()
fp1.close()
from nltk.corpus import stopwords
english_stops = set(stopwords.words('english'))
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
filename="whole_review_with_adv_adj_only_final.txt"
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
filename1="new_intermidiate_tokenized_with_stopwords-removed_and_stemming_done.txt"
filename="new_neg_complete_tokenized_with_stopwords-removed_and_stemming_done.txt"
filename3="new_pos_complete_tokenized_with_stopwords-removed_and_stemming_done.txt"
filename4="output_scaled_analyzed_reviews_without_dict.txt" #here this is the ouput file
f=open(filename,'r')
_listneg=[]
while True:
    line=f.readline()
    if not line:
        break
    token=line.strip().split('\n')
    b=token[0]
    b=b.lower()
    _listneg.append(b);
f.close()
f3=open(filename3,'r')
_listpos=[]
while True:
    line=f3.readline()
    if not line:
        break
    token=line.strip().split('\n')
    b=token[0]
    b=b.lower()
    _listpos.append(b);
#print _listpos
f3.close()
f1=open(filename1,'r')
f4=open(filename4,'w')
cou=0
coups=0
coung=0
while True:
    line=f1.readline()
    if not line:
        break
    token=line.strip().split(' ')
    i=0
    count=0
    while True:
        if(i>=len(token)):
            break
        a=str(token[i])
        cou=cou+1
        if a in _listpos :
            coups=coups+1
            count=count+1
        if a in _listneg:
            coups=coups-1#counng=coung-1
            count=count-1
        i=i+1
    f4.write("score: "+str(count)+";    scaled score: "+ (str((count*5.0)/len(token))+"\n"))
print coups
print coung
f4.write("\n TOTAL words "+str(cou)+"; scaled score:"+str(((coups)*5.0)/cou))
f1.close()
f4.close()