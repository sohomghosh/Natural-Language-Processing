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
        #fp1.write(str( token)+"\n")
#        print token[1]
#    if len(token)>0:
 #       if token[1]=='RBS':

        fp1.write(str( token[0])+" "+token[1]+"\n")
fp.close()
fp1.close()