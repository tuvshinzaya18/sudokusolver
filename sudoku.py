def check0(table):
    checker=False
    for row50 in table:
        for cell50 in row50:
            if cell50==0:
                checker=True
    return checker
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
def checkrow(row,tablerow):
    table=tablerow
    numbers=[1,2,3,4,5,6,7,8,9]
    for column in range(0,9):
        num=table[row][column]
        if num in numbers:
            numbers.remove(num)
    return numbers
def checkcolumn(column,tablerow):
    table=tablerow
    numbers=[1,2,3,4,5,6,7,8,9]
    for row in range(0,9):
        num=table[row][column]
        if num in numbers:
            numbers.remove(num)
    return numbers
def checkbox(box,tablebox):
    global boxfindnew
    table=tablebox
    cord=boxfindnew[box]
    numbers=[1,2,3,4,5,6,7,8,9]
    for xy in cord:
        row=xy[0]
        column=xy[1]
        num=table[row][column]
        if num in numbers:
            numbers.remove(num)
    return numbers
#first function uses checking possible positions for target number
def first(tablefirst,boxfindfirst,full):
    checkerbig=False
    table=tablefirst
    boxfind=boxfindfirst
    boxfindfull=full
    for i in range(0,9):
            coordinates10=boxfindfull[i]
            for cords10 in coordinates10:
                row20=cords10[0]
                column20=cords10[1]
                numb=table[row20][column20]
                if numb in [1,2,3,4,5,6,7,8,9]:
                    boxfind[i].remove([row20,column20])
    while True:
        checker2=False
        checker1=True
        for i in range(0,9):
            numbers=[1,2,3,4,5,6,7,8,9]
            coordinates=boxfindfull[i]
            for cords in coordinates:
                row10=cords[0]
                column10=cords[1]
                numb=table[row10][column10]
                if numb in [1,2,3,4,5,6,7,8,9]:
                    numbers.remove(numb)
            for n in numbers:
                possiblepos=[]
                possiblepos.clear()
                newcords=boxfind[i]
                for newxy in newcords:
                    checker = True
                    nrow=newxy[0]
                    ncolumn=newxy[1]
                    for c1 in range(0,9):
                        if table[nrow][c1] == n:
                            checker=False
                    for r1 in range(0,9):
                        if table[r1][ncolumn] == n:
                            checker=False
                    if checker == True:
                        possiblepos.append([nrow,ncolumn])
                if len(possiblepos) == 1:
                    table[possiblepos[0][0]][possiblepos[0][1]]=n
                    boxfind[i].remove([possiblepos[0][0],possiblepos[0][1]])
                    checker2=True
                    checkerbig=True
        for box in boxfind:
            if len(box)!=0:
                checker1=False
        if checker1 == True:
            break
        if checker2 == False:
            break
    answer=[]
    answer.append(table)
    answer.append(boxfind)
    answer.append(checkerbig)
    return answer
#second function uses elimination method to further solve sudoku
def second(tablesec,boxfindsec):
    checkerbig1=False
    boxfind=boxfindsec
    table=tablesec
    while True:
        checker3=False
        checker1=True
        i=0
        checkboxfind=boxfind
        for box in boxfind:
            for cordinate in box:
                posnumber=[]
                row=cordinate[0]
                col=cordinate[1]
                rowpos=checkrow(row,table)
                colpos=checkcolumn(col,table)
                boxpos=checkbox(i,table)
                for posnum in range(1,10):
                    if posnum in rowpos and posnum in colpos and posnum in boxpos:
                        posnumber.append(posnum)
                if len(posnumber) ==1:
                    checkerbig1=True
                    checker3=True
                    boxfind[i].remove([row,col])
                    table[row][col]=posnumber[0]
            i+=1
        for box1 in boxfind:
            if len(box1)!=0:
                checker1=False
        if checker1 == True:
            break
        if checker3 == False:
            break
    answer=[]
    answer.append(table)
    answer.append(boxfind)
    answer.append(checkerbig1)
    return answer
def main(table):
    global boxfindnew
    returnanswer=False
    #boxfind keeps track of empty cells
    boxfind=[]
    for i in range(0,9):
        boxfind.append([])
    for i in range(0,9):
        for n in range(0,9):
            boxn=(i//3)*3+n//3
            boxfind[boxn].append([i,n])
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
#table[i][n] i-row n-column
table=[]
for i in range(0,9):
    table.append([])
tableraw=""
boxfindnew=[]
for i in range(0,9):
    boxfindnew.append([])
for i in range(0,9):
    for n in range(0,9):
        boxn=(i//3)*3+n//3
        boxfindnew[boxn].append([i,n])
for i in range(0,9):
    tableraw+=input("")
count=0
for i in range(0,9):
    for n in range(0,9):
        table[i].append(int(tableraw[count]))
        count+=1
main(table)