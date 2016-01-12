from nltk.corpus import stopwords
english_stops = set(stopwords.words('english'))
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
filename="new_whole_review_tokenized_with_stopwords-removed_and_stemming_done.txt"
filename2="mispelt_removed_whole_review_tokenized_with_stopwords-removed_and_stemming_done.txt";
f=open(filename,"r");
f2=open(filename2,"w");
tel={'rang':'range', 'volum':'volume','packag':'package','strech':'stretch','littl':'little','averag':'average','satisfactori':'satisfactory','valu':'value','capabl':'capable','thi':'this','entri':'entry','galaxi':'galaxy','happi':'happy','mobil':'mobile','thi':'this','awesom':'awesome','upgrad':'upgrade','batteri':'battery','els':'else','devic':'device','entri':'entry','smartphon':'smart phone','everi':'every','rupe':'rupee','middl':'middle','thi':'this','mobil':'mobile','entri':'entry','overal':'overall','experi':'experience','galaxi':'galaxy','duo':'duos','anoth':'another','ripoff':'rip off','batteri':'battery','deliv':'delivery','rang':'range','dou':'duos','valu':'value','daili':'daily','basi':'basically','pretti':'pretty','improv':'improve','veri':'very','biggin':'beginning','confid':'confidence','awesom':'awesome','deliveri':'delivery','experi':'experiment','mobil':'mobile','valu':'value','purchas':'purchase','clos':'close','ur':'your','amaz':'amaze','unbeliev':'unbelief','thi':'this','awsm':'awesome','owwsom':'awesome','captur':'capture','onlin':'online','featur':'feature','simpli':'simply','gener':'general','nexu':'nexus','usag':'usage','rang':'range','qualiti':'quality','assur':'assure','replac':'replace','servic':'service','satisfi':'satisfy','packag':'package','faulti':'faulty','availabl':'available','warranti':'warranty','superbb':'superb','issu':'issue','devil':'delivery','promis':'promise','googl':'google','decis':'decision','evarrrrrrrrrrrrrrrrrrrrrrrr':'ever','choos':'choose','varieti':'variety','fantast':'fantastic','rang':'range','updat':'update','piec':'piece','thnk':'thank','u':'you','absolut':'absolute','deliv':'deliver','everyth':'everything','beginn':'begin','servic':'service','realli':'really','shitti':'shitty','gen':'generation','silki':'silky','includ':'include','altern':'alternate','reali':'realize','worthi':'worthy','certifi':'certify','sensibl':'sensible','perefct':'perfect','veri':'very','hardwar':'hardware','awstruck':'awestruck','fulli':'fully','deliveri':'delivery','releas':'release','overal':'overall','configur':'configuration','valu':'value','issu':'issue','warranti':'warranty','provid':'provide','packag':'package','lapi':'lapy','excil':'excellent','handl':'handle','singl':'single','describ':'describe','busi':'busy','lovin':'loving','latitud':'latitude','workhors':'work hours','deliv':'delivery','websit':'website','probabl':'probably','exactli':'exactly','promis':'promise','applic':'applicable','effici':'efficiency','anyth':'anything','peopl':'people','unawar':'unaware','that..unfortun':'unfortunate','alll':'all','costli':'costly','superfin':'superfine','qualiti':'quality','choic':'choice','amazingli':'amazingly','purchas':'purchase','mobil':'mobile','decis':'decision','featur':'feature','someth':'something','worthi':'worthy','im':'i am','luving':'loving','beauti':'beauty','escap':'escape','anyth':'anything','littl':'little','improv':'improve','radiat':'radiation','issu':'issue','precis':'precise','appreci':'appreciate','piec':'piece','pleas':'please','littl':'little','reduc':'reduce','whi':'while','experi':'experiment','decis':'decision','troubl':'trouble','conveni':'convenient','smartphon':'smart phone','Duo':'duos','failur':'failure','batteri':'battery','heavi':'heavy','mani':'money','laggeri':'lag','laggardli':'lag','featur':'feature','por':'poor','minu':'minus','charg':'charge','usabl':'usable','memori':'memory','compon':'component','discharg':'discharge','th':'the','bbad':'bad','reciv':'receive', 'damag':'damage','wast':'waste','initi':'initial','17amazingli':'amazingly','canva':'canvas','doodl':'doodle','cam':'camera','whatta':'what a','superbbb':'superb','evarrrrrrrrrrrrrrrrrrrrrrrrrr':'ever','doe':'do','abov':'above','awesum':'awesome','complet':'complete','fargreat':'far great','satisfacori':'satisfactory','compar':'compare','overal':'overall','avaibl':'available','practic':'practise','valu':'value','--valu':'negative value','ammmaaz':'amaze','awstruck!':'awestruck','thi':'this','hurri':'hurry','tremend':'tremendous','confid':'confidence','happi':'happy','clos':'close','amaze':'amaze','rang':'range','noth':'no','experi':'experience','worh':'worth','wordto':'word to','radiat':'radiant','whi':'while','disadvantag':'disadvantage','troubl':'trouble','conveni':'convenient','dwindl':'dwindle','dont':'do not','laggy':'lag','pathet':'phablet','onli':'only','receiv':'receive','insuffici':'insufficient','accessori':'accessory','capac':'capacity','unstabl':'unstable','easi':'easy','stori':'story'}
while True:
	line=f.readline()
        if not line:
           break
        _token=line.strip().split(' ')
        i=0
        while True:
            b=_token[i]
            b=b.lower()
            k=b in tel
            if k== True:
                b=tel[b]
            #str(tel[str(b)])
            f2.write( str(b)+" ")
            #print b
            #print b
            #b=str(tel[_token[i]])
            i=i+1
            if(i==len(_token)) :
                break
        f2.write("\n")

f.close()
f2.close()
