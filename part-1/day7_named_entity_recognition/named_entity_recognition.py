import nltk
filename="whole_review.txt"
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