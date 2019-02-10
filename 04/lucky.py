from os import system as term
fastcollCommand="./fastcoll/fastcoll"
N=6
destDir="collisions"
tempDir="collissions/coll"
suffix=destDir+"/suffix"
prefix=destDir+"/prefix"
prefix_head="%!PS-Adobe-1.0\n/blob ("
prefix_Tail=") def\n"

ifHead="blob ("
IF_CLAUSE_POST=") eq\n{"

ELSEifHead="} if\nblob ("
elseifHead=") eq\n{"

elseHead="} if{\n"

ending="}\nshowpage"

def getCode(x):
    return "/Times-Roman findfont 64 scalefont setfont \n 30 200 moveto\n(Saif and Kibria guess % s) show\n"+ str(x)
def getFileName(x):
    return "file_"+str(x)+".ps"
def setPrefix():
    term("echo -ne "+"\""+prefix_head+"\""+" > "+prefix)
def init():
    term("mkdir -p "+destDir)
    term("mkdir -p "+tempDir)
def getCollisions():
    term(fastcollCommand+" -p "+prefix+" o "+tempDir+"/0 "+tempDir+"/1")
    for i in range(1,N+1):
        t=bin(pow(2,i)-1)
        term(fastcollCommand +  " -p "+ tempDir+"/"+str(t) +\
                           "-o "+tempDir+"/tmp.full.0 " + tempDir+"/tmp.full.1")
        term("tail -c 128 "+tempDir+"/tmp.full.0 > "+tempDir+ "/tmp.0")
        term("tail -c 128 "+ tempDir+"tmp.full.1 > "+tempDir+"/tmp.1")
        for j in range(int(t,2)):
            te=bin(j)
            term("echo Generating intermidiate collision "+te)

            term("cp"+tempDir+"/"+str(te)+" "+tempDir+"/"+str(te)+"0")
            term("cat"+tempDir+"/tmp.0 >> "+tempDir+"/"+te+"0")
            term("cp" + tempDir + "/" + str(te) + " " + tempDir + "/" + str(te) + "1")
            term("cat "+tempDir+"/tmp.1 >> "+tempDir+"/"+str(te)+"1")
    totalFiles=pow(2,N)-1
    prefixSize=len(prefix_head)
    for i in range(totalFiles):
        t=bin(i)
        term("cp "+tempDir+"/"+str(t)+" "+destDir+" "+getFileName(i))
        term("dd if="+tempDir+"/"+str(t)+" "+"of="+tempDir+"blob_"+str(i)+" bs=1 skip="+str(prefixSize))

def getSuffix():
    term("echo -ne "+prefix_Tail+" >> "+suffix)
    term("echo -ne " + ifHead + " >> " + suffix)
    term("cat "+tempDir+"/blob_1 >> "+suffix)
    term("echo -ne " + IF_CLAUSE_POST + " >> " + suffix)
    term("echo -ne " + getCode(1) + " >> " + suffix)
    for i in range(2,pow(2,N)):
        term("echo -ne " + ELSEifHead + " >> " + suffix)
        term("cat " + tempDir + "/blob_"+str(i)+" >> " + suffix)
        term("echo -ne " + elseifHead + " >> " + suffix)
        term("echo -ne " + getCode(i) + " >> " + suffix)


    term("echo -ne " + ending + " >> " + suffix)
def appendSuffix():
    for i in range(pow(2,6)):
        term("cat  "+tempDir+"/suffix >> "+destDir+"/"+getFileName(i))
def do():
    init()
    setPrefix()
    getCollisions()
    getSuffix()
    appendSuffix()
i=1
while(True):
    do()
    x=term("ghostscript collisions/file_1.ps")
    print(i)
    i+=1
    if x==0:
        break
