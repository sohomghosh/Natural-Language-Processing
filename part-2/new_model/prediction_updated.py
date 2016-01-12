user_iput_movie_name=raw_input("Enter the name of the movie")
movie_name=str(user_iput_movie_name)+".txt"
movie_name_tomatometer=str(user_iput_movie_name)+"tomatometer.txt"

user_input_review_title=raw_input("Please write the title of the review")
f=open("review_title_input.txt",'w')
f.write(str(user_input_review_title)+"")
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
        #print a
        a=a.strip()
        a=a.lower()
        if a in _listpos :
            count=count+1
            #print "here"
        if a in _listneg:
            #print "here"
            count=count-1
        i=i+1
    #count=(count/i)*5.0
    #print len(token)
    #print count
    f4.write( (str(round(((count*1.000000)/len(token)),2))+"\n"))
f1.close()
f4.close()
filename4="new_scaled_analyzed__review_title_without_dict.txt"
f4=open(filename4,'r')
line=f4.readline()
a=line.strip()
f4.close()
#print a
_list=[]##
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
        ##_list= "Suggestions for u"
        for i in range(1,len(token)):
            _list.append(token[i])
           ## print str(token[i])##
        _list.append(";These are suggestions for you, Enter ur review:")
        break
if flag==0:
    _list="sorry no suggestions for u; Enter ur review: "
    ##print "\nsorry no suggestions for u\n"##
userinput = raw_input(str(_list))##"enter ur review"##

f6=open("input_whole_review_test2.txt",'w')
f6.write(str(userinput)+"")
f6.close()



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
count=0
filename="whole_review_with_adv_adj_only_intermediate.txt"
f=open(filename,'r')
fp1=open("whole_review_with_adv_adj_only_final.txt",'w')
while True:
    line=f.readline()
    if not line:
        break
    token=line.strip().split(' ')
    for i in range(1,len(token)):
        q=str(token[i])
        _token=q.strip().split('/')
        #print _token
        if _token[1]=='RBS' or _token[1]=='RBR' or _token[1]=='RB' or _token[1]=='JJS' or _token[1]=='JJR' or _token[1]=='JJ':
            #print _token[0]
            fp1.write(_token[0]+"\n")
            count=count+1
f.close()
fp1.close()


fp1=open("whole_review_with_adv_adj_only_final.txt",'r')
userinput=fp1.readline()
fp1.close()
#print userinput
fp.close()
if flag==0 and count!=0:
    #print ("control here")
    fp=open("database.csv",'a')
    fp.write(str(a)+",")
    fp1=open("whole_review_with_adv_adj_only_final.txt",'r')
    ab=str(fp1.readline())
    _token=ab.strip().split(' ')
    print _token
    for i in range(0,len(_token)):
        fp.write(str(_token[i])+",")
    fp.write("\n")
    fp.close()








import nltk
from nltk.stem import PorterStemmer


#keeping one line one sent
filename="input_whole_review_test2.txt"#input file replace by input_whole_review_test2.txt
filename1="each_line_one_sent.txt"
fp1=open(filename1,'w')
fp=open(filename,'r')
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
        a=a.strip()
        a=a.lower()
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
    #print count
    #print count1
if count1!=0:
    a= (round((count*1.00/count1),2))
else:
    a=0
#print a
k=0
if a>=-1 and a<-.8 :
    k=1
if a>=-.8 and a<-.6:
    k=2
if a>=-.6 and a<-.4:
    k=3
if a>=-.4 and a<-.2:
    k=4
if a>=-.2 and a<0:
    k=5
if a>=0 and a<.2:
    k=6
if a>=.2 and a<.4:
    k=7
if a>=.4 and a<.6:
    k=8
if a>=.6 and a<.8:
    k=9
if a>=.8 and a<=1:
    k=10

aa=str(k)
user_score_input=raw_input("your rating is likely to be"+aa+".  Enter your rating from 1 to 10")
fp.close()


f=open(movie_name,'a')
f.write(str(user_score_input)+"\n")
f.close

f8=open(movie_name_tomatometer,'a')
f=open(movie_name,'r')
count=0
sum=0
while True:
    line=f.readline()
    if not line:
        break
    token=line.strip().split(' ')
    #print token[0]
    q=(str(token[0]))
    qq=int(q)
    if(qq>=7): #a movie with rating above 7 is considered as positive by rotten tomato
        f8.write("+1\n")
    else:
        f8.write("-1\n")
   # print q
    sum=sum+int(q)
    count=count+1
f.close()
f8.close()

a= (sum*1.0)/count
imdb=((sum+175000)*1.0)/((count+25000)*1.0) #As per IMDb's formula
print "Overall rating as per IMDb's scoring system is: "+str(round(imdb,1))
if imdb>=0 and imdb<2:
    print "As per imdb's way score calculation Movie is superflop"
if imdb>=2 and imdb<4:
    print "As per imdb's way score calculation Movie is flop"
if imdb>=4 and imdb<6:
    print "As per imdb's way score calculation Movie is cool"
if imdb>=6 and imdb<8:
    print "As per imdb's way score calculation Movie is hit"
if imdb>=8 and imdb<=10:
    print "As per imdb's way score calculation Movie is superhit"
print "Overall rating as per our scoring system is: "+str(round(a,1))
if a>=0 and a<2:
    print "As per scoring our system Movie is superflop"
if a>=2 and a<4:
    print "As per scoring our system Movie is flop"
if a>=4 and a<6:
    print "As per scoring our system Movie is cool"
if a>=6 and a<8:
    print "As per scoring our system Movie is hit"
if a>=8 and a<=10:
    print "As per scoring our system Movie is superhit"

#Tomatometer
f8=open(movie_name_tomatometer,'r')
cp=0
ct=0
while True:
    line=f8.readline()
    if not line:
        break
    ct=ct+1
    token=line.strip().split(' ')
    #print len(token)
    if(len(token)>=1 and token[0]=='+1'):
        cp=cp+1
#print cp
#print ct
kk=((cp*1.0)/ct)*100
if(kk>=60):
    print "As per the scoring system of Rotten Tomatoes The Movie is fresh"
else:
    print "As per the scoring system of Rotten Tomatoes The movie is rotten"