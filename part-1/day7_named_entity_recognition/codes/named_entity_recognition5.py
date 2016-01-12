filename1="new_intermidiate_tokenized_with_stopwords-removed_and_stemming_done.txt"
filename="new_neg_complete_tokenized_with_stopwords-removed_and_stemming_done.txt"
filename3="new_pos_complete_tokenized_with_stopwords-removed_and_stemming_done.txt"
filename4="scaled_analyzed_positive_reviews_without_dict.txt"
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
            count=count+1
            coups=coups+1;
        if a in _listneg:
            count=count-1
            counng=coung-1;
        i=i+1
    #count=(count/i)*5.0
   # print (count*5.0)/len(token)
    f4.write("score: "+str(count)+";    scaled score: "+ (str((count*5.0)/len(token))+"\n"))
f4.write("\n TOTAL SCORE "+str(cou)+"; scaled score:"+str(((coups-coung)*5.0)/cou))
f1.close()
f4.close()