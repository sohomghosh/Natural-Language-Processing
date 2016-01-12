filename1="mispelt_removed_negative_reviews_tokenized_with_stopwords-removed_and_stemming_done.txt"
filename="neg_complete.txt"
filename3="pos_complete.txt"
filename4="analyzed_neg_reviews_new.txt"
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
    f4.write(str(count)+"\n")
f1.close()
f4.close()