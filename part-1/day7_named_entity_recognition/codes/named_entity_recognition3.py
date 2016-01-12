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
    #print token
    if len(token)>1:
        if token[1]=='RBS' or token[1]=='RBR' or token[1]=='RB' or token[1]=='JJS' or token[1]=='JJR' or token[1]=='JJ':
            fp1.write(token[0]+"\n")
fp.close()
fp1.close()