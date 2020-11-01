import random
numbers=list(range(1,10))
poslocs=[]
for i in range(0,9):
    for n in range(0,9):
        poslocs.append([i,n])
def printtable(table):
    n=0
    for row in table:
        i=0
        text=""
        for cell in row:
            if i==2 or i==5:
                text+=str(cell)+"|"
            else:
                text+=str(cell)
            i+=1
        print(text)
        if n==2 or n==5:
            print("-----------")
        n+=1
def texttable(table):
    hugetext=""
    n=0
    for row in table:
        i=0
        text=""
        for cell in row:
            if i==2 or i==5:
                text+=str(cell)+"|"
            else:
                text+=str(cell)
            i+=1
        hugetext+=text+"\n"
        if n==2 or n==5:
            hugetext+="-----------\n"
        n+=1
    return hugetext
base=random.sample(numbers,9)
def move(base,n):
    newbase=[]
    length=len(base)
    for i in range(length-n,length):
        newbase.append(base[i])
    for i in range(0,length-n):
        newbase.append(base[i])
    return newbase
table=[]
for i in range(0,9):
    n=i//3+(i%3)*3
    table.append(move(base,n))
def shuffle9():
    origin=list(range(0,9))
    sec3=[origin[0:2],origin[3:5],origin[6:8]]
def shuffle(pos):
    return random.sample(pos,len(pos))
def shuffle9():
    origin=list(range(0,9))
    sec3=[origin[0:3],origin[3:6],origin[6:]]
    for i in range(0,3):
        sec3[i]=shuffle(sec3[i])
    sec3=shuffle(sec3)
    newli=[]
    for sec in sec3:
        for n in sec:
            newli.append(n)
    return newli
def rowshuf(table):
    order=shuffle9()
    newtable=[]
    for n in range(0,9):
        newtable.append([])
    count=0
    for i in order:
        newtable[count]=table[i]
        count+=1
    return newtable
def colshuf(table):
    order=shuffle9()
    newtable=[]
    for n in range(0,9):
        newtable.append([])
    count=0
    for i in order:
        for row in range(0,9):
            newtable[row].append(table[row][i])
    return newtable

def mainish(table):
    returnanswer=False
    #boxfind keeps track of empty cells
    boxfind=[]
    for i in range(0,9):
        boxfind.append([])
    for i in range(0,9):
        for n in range(0,9):
            boxn=(i//3)*3+n//3
            boxfind[boxn].append([i,n])
    boxfindnew=[]
    for i in range(0,9):
        boxfindnew.append([])
    for i in range(0,9):
        for n in range(0,9):
            boxn=(i//3)*3+n//3
            boxfindnew[boxn].append([i,n])
    #boxfindnew contains list of cords of cells for each boxs 
    while True:
        checkerforsure=False
        answer1=first(table,boxfind,boxfindnew)
        table=answer1[0]
        boxfind=answer1[1]
        checkerbiggest=answer1[2]
        if checkerbiggest:
            checkerforsure=True
        answer2=second(table,boxfind)
        table=answer2[0]
        boxfind=answer2[1]
        checkerbiggest1=answer2[2]
        if checkerbiggest1:
            checkerforsure=True
        if not check0(table):
            returnanswer=True
            print("solved")
            break
        if not checkerforsure:
            returnanswer=False
            print("can't solve it")
            break
            
    printtable(table)
    return returnanswer
for i in range(0,3):
    table=rowshuf(table)
    table=colshuf(table)
try:
    f1=open("results.txt","x")
    f1.close()
except:
    nothing=0
f2=open("results.txt","a")
f2.write(texttable(table))
f2.close()
#choose level of sudoku
while True:
    print("choose level of sudoku:\n1.Easy\n2.Medium")
    level=input("Answer?:")
    if level in "12":
        break
    print("wrong answer")
if level =="1":
    emptynum=38
else:
    emptynum=48
restable=table
dellocs=random.sample(poslocs,emptynum)
for xys in dellocs:
    row=xys[0]
    col=xys[1]
    restable[row][col]=0
printtable(restable)
#shuffle boxs relative to rows
