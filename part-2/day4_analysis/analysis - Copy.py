import nltk
from nltk.stem import PorterStemmer


#keeping one line one sent
filename="20.txt"#input file replace by input_whole_review_test2.txt
filename1="each_line_one_sent.txt"
fp1=open(filename1,'w')
fp=open(filename,'r')
line=fp.readline()
while True:
    line=fp.readline()
    if not line:
        break
    token=line.strip().split('. ')
    for i in range(0,len(token)):
        fp1.write(str(token[i])+"\n")
fp1.close()
fp.close()


#only adj adv detect; stemmeing using porter stemmer
fp=open("only_adj_adv.txt",'w')
filename1="each_line_one_sent.txt"
fp1=open(filename1,'r')
while True:
    line=fp1.readline()
    if not line:
        break
    token=line.strip().split(' ')
    a=nltk.pos_tag(token)
    for i in range(0,len(a)):
        q=a[i][1]
        if q=='RBS' or q=='RBR' or q=='RB' or q=='JJS' or q=='JJR' or q=='JJ':
            ng=PorterStemmer().stem(a[i][0])
            fp.write(str(ng)+";"+str(i)+" ")
    fp.write("\n")
fp1.close()
fp.close()


#replace pos word by +1 neg word by -1
filename1="only_adj_adv.txt"
filename="new_neg_complete_tokenized_with_stopwords-removed_and_stemming_done.txt"
filename3="new_pos_complete_tokenized_with_stopwords-removed_and_stemming_done.txt"
filename4="pos_neg_word_replace_by_value.txt" #here this is the ouput file
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
        _token=a.split(';')
        a=_token[0]
        #if len(_token)>1:
         #   print _token[1]
        if a in _listpos :
            if len(_token)>1:
                f4.write("+1,"+str(_token[1])+";")
        if a in _listneg:
            if len(_token)>1:
                f4.write("-1,"+str(_token[1])+";")
        i=i+1
    f4.write("\n")
f1.close()
f4.close()


#score calculation without hierchial concept
fp=open("pos_neg_word_replace_by_value.txt",'r')
count=0
count1=0
while True:
    line=fp.readline()
    if not line:
        break;
    token=line.strip().split(';')

    for i in range(0,len(token)):
        _token1=str(token[i]).split(',')
        if _token1[0]=='+1':
            count=count+1
            count1=count1+1
        if _token1[0]=='-1':
            count=count-1
            count1=count1+1
a= (round((count*1.00/count1),2))
k=0
if a>=-1 and a<-.6 :
    k=1
if a>=-.6 and a<-.2:
    k=2
if a>=-.2 and a<+.2:
    k=3
if a>=+.2 and a<+.6:
    k=4
if a>=+.6 and a<+1:
    k=5
aa=str(k)
user_score_input=raw_input("your rating is likely to be"+aa+".  Enter your rating from 1 to 5")
fp.close()


f=open("all_score.txt",'a')
f.write(str(user_score_input)+"\n")
f.close


f=open("all_score.txt",'r')
count=0
sum=0
while True:
    line=f.readline()
    if not line:
        break
    sum=sum+int(line)
    count=count+1
f.close()
a= sum/count
if a==1:
    print "Movie is superflop"
if a==2:
    print "Movie is flop"
if a==3:
    print "Movie is cool"
if a==4:
    print "Movie is hit"
if a==5:
    print "Movie is superhit"