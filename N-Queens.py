import random
import timeit

def readFile(rec):  # read the file
    file = open("n-queen.txt","r")
    for line in file:
        rec.append(line.split())
    file.close()
    return

def writeFile(rec):  # write the solution
    file1 = open("out.txt","w")
    for singleRec in rec:
        stringRec = '   '.join(singleRec)
        file1.write(stringRec + "\n")
    file1.close()
    return

def conflictQueens(rec, a, b):  # count the number of queens that have conflicts with Queen[a][b]
    num = 0
    for i in range(0,len(rec[0])):  # count the number in a row
        if rec[a][i] == str(1) and i != b:
            num = num + 1
    j = a + 1
    k = b + 1
    while 0<=j<len(rec[0]) and 0<=k<len(rec[0]):  # reverse right diagonal
        if  rec[j][k] == str(1):
            num = num + 1
        j = j + 1
        k = k + 1
    j = a - 1
    k = b - 1
    while 0<=j<len(rec[0]) and 0<=k<len(rec[0]):  # forward left diagonal
        if  rec[j][k] == str(1):
            num = num + 1
        j = j - 1
        k = k - 1
    j = a + 1
    k = b - 1
    while 0<=j<len(rec[0]) and 0<=k<len(rec[0]):  # reverse left diagonal
        if  rec[j][k] == str(1):
            num = num + 1
        j = j + 1
        k = k - 1
    j = a - 1
    k = b + 1
    while 0<=j<len(rec[0]) and 0<=k<len(rec[0]):  # forward right diagonal
        if  rec[j][k] == str(1):
            num = num + 1
        j = j - 1
        k = k + 1
    return num

def reduceConflicts(rec, b):  # find the location which has the minimum conflicts
    row = []
    columnconflicts = []
    lowestconflicts = len(rec[0])
    for i in range(0, len(rec[0])):
        columnconflicts.append(conflictQueens(rec, i, b))
        if columnconflicts[i] <= lowestconflicts:
            lowestconflicts = columnconflicts[i]
    for j in range(0, len(rec[0])):
        if columnconflicts[j] == lowestconflicts:
            row.append(j)
    end = len(row) - 1
    k = random.randint(0, end)
    return row[k]

def findQueen(rec, b):  # return the location of a queen in a column
    for i in range(0, len(rec[0])):
        if rec[i][b] == str(1):
            a = i
            break
    return a

def countConflicts(rec):  # return the number of all conflicts in a board
    conflicts = 0
    for i in range(0, len(rec[0])):
        a = findQueen(rec, i)
        conflicts = conflicts + conflictQueens(rec, a, i)
    return conflicts

def conflictbiggest(rec):  # return a random column with the biggest conflicts
    conflictsrow = []
    biggestb = -1
    ran = []
    for i in range(0, len(rec[0])):
        a = findQueen(rec, i)
        conflictsrow.append(conflictQueens(rec, a, i))
        if biggestb <= conflictsrow[i]:
            biggestb = conflictsrow[i]
    for j in range(0, len(rec[0])):
        if conflictsrow[j] == biggestb:
            ran.append(j)
    end = len(ran) - 1
    k = random.randint(0, end)
    return ran[k]

def findSolution(rec):
    end = len(rec[0]) - 1
    conflicts = end
    move = 0
    count = 0
    c = -1
    while conflicts != 0:
        b = conflictbiggest(rec)  # take a random column with the biggest conflicts
        while c == b:  # guarantee that the random number taken this time is different from the random number taken last time
            b = conflictbiggest(rec)
        a = findQueen(rec, b)
        newrow = reduceConflicts(rec, b)
        if a != newrow:
            print("Step: move Queen([" + str(a) + "][" + str(b)  + "]) to Location([" + str(newrow) + "][" + str(b)  + "])")
            rec[a][b] = str(0)
            rec[newrow][b] = str(1)
            move = move + 1
            count = count + 1
            conflicts = countConflicts(rec)
            print("Conflicts: " + str(conflicts))
            print("Moves: " + str(move))
        else:
            move = move
            count = count + 1
            conflicts = countConflicts(rec)
        c = b

def main():
    start = timeit.default_timer()
    rec = []
    readFile(rec)
    findSolution(rec)
    writeFile(rec)
    stop = timeit.default_timer()
    time = stop - start
    print("Time: " + str(time) + "s")
    print("See the solution in the file(out.txt).")

main()
