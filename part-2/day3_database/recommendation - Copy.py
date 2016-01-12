user_input_review_title=raw_input("Please write the title of the review")
f=open("review_title_input.txt",'w')
f.close()
from nltk.corpus import stopwords
english_stops = set(stopwords.words('english'))
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
filename="review_title_input.txt" #replace input_file by your own file name
filename2="new_intermidiate_tokenized_with_stopwords-removed_and_stemming_done.txt"; #this is the intermediate file
f=open(filename,'r');
f2=open(filename2,'w');
while True:
    line=f.readline()
    if not line:
        break
    _token=[stemmer.stem(i) for i in line.split() if i not in english_stops]
#print(_token)
    i=0
    while i<len(_token) :
    #print i
        f2.write( str(_token[i])+" ")
        i=i+1
    f2.write("\n")
f.close()
f2.close()
filename1="new_intermidiate_tokenized_with_stopwords-removed_and_stemming_done.txt"
filename="new_neg_complete_tokenized_with_stopwords-removed_and_stemming_done.txt"
filename3="new_pos_complete_tokenized_with_stopwords-removed_and_stemming_done.txt"
filename4="new_scaled_analyzed__review_title_without_dict.txt"
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
while True:
    line=f1.readline()
    if not line:
        break
    token=line.strip().split(' ')

    #print(token)
    i=0
    count=0
    while True:
        if(i>=len(token)):
            break
        a=str(token[i])
        if a in _listpos :
            count=count+1;
        if a in _listneg:
            count=count-1;
        i=i+1
    #count=(count/i)*5.0
   # print (count*5.0)/len(token)
    f4.write( (str(round(((count*1.0)/len(token)),2))+"\n"))
f1.close()
f4.close()
filename4="new_scaled_analyzed__review_title_without_dict.txt"
f4=open(filename4,'r')
line=f4.readline()
a=line.strip()
f4.close()
#print a
filename="database.csv"
fp=open(filename,'r')
flag=0
while True:
    line=fp.readline()
    if not line:
        break
    token=line.strip().split(',')
    if token[0]==a:
        flag=1
        print "\nSuggestions for u\n"
        for i in range(1,len(token)):
            print str(token[i])
        break
if flag==0:
    print "\nsorry no suggestions for u\n"
userinput = raw_input("\nEnter ur review \n ")
#print userinput
fp.close()
if flag==0:
    #print ("control here")
    fp=open("database.csv",'a')
    fp.write(str(a)+",")
    ab=str(userinput)
    _token=ab.strip().split(' ')
   # print _token
    for i in range(0,len(_token)):
        fp.write(str(_token[i])+",")
    fp.write("\n")
