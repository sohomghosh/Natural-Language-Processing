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
    #print token[0]
    fp1.write(str( token[0])+"\n")
fp.close()
fp1.close()