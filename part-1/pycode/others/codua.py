f1=open('negative_reviews_sam.txt','r');
f2=open('negative_reviews_sam_new.txt','w');
while True:
    line1=f1.readline()
    line1.strip()
    if not line1:
        break
    from nltk.corpus import stopwords
    english_stops = set(stopwords.words('english'))
    words = [line1]
    f2.write(words)
    #f2.write(str(line1.split(' ')[0]))
f1.close()
f2.close()
