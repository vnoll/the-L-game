import drawTable as dt
import random

def tableWithoutBlue(table, color):

    kblue = [key for key, value_kvoid in table.items() if value_kvoid == color]
    print kblue
    for item in kblue:
        table[item] = "void"
    return table,kblue

def sameline(pa,pb):
    if pa in range(1,5):
        if pb in range(1,5):
            return True
    if pa in range(5,9):
        if pb in range(5,9):
            return True
    if pa in range(9,13):
        if pb in range(9,13):
            return True
    if pa in range(13,17):
        if pb in range(13,17):
            return True
    return False

def samecolumn(pa,pb):
    if pa + 4 == pb:
            return True
    if pa - 4 == pb:
            return True
    return False

def findPossiblesL(table_adj):

    # print " "
    # print "[13 14 15 16]  [a4 b4 c4 d4]"
    # print "[09 10 11 12]  [a3 b3 c3 d3]"
    # print "[05 06 07 08]  [a2 b2 c2 d2]"
    # print "[01 02 03 04]  [a1 b1 c1 d1]"
    # print " "

    numeric_table={'a1':1,'b1':2,'c1':3,'d1':4,'a2':5,'b2':6,'c2':7,'d2':8,'a3':9,'b3':10,'c3':11,'d3':12, 'a4':13,'b4':14,'c4':15,'d4':16}
    kvoid = [key for key, value in table_adj.items() if value == 'void']
    
    value_kvoid = []
    for item in kvoid:
        value_kvoid.append(numeric_table[item])

    markAsHor = []
    achei1D = False
    for item in value_kvoid:
        for x in value_kvoid:
            if x == item + 1:
                achei1D = True
        if achei1D == True:
            achei1D = False
            for y in value_kvoid:
                if y == item -1: 
                    if item == 2 or item == 3 or item == 6 or item ==7 or item == 10 or item == 11 or item == 14 or item == 15:
                        markAsHor.append(item)

    ## print markAsHor

    possibleLHor = []
    for item in markAsHor:
        point_a = item - 3
        point_b = item - 5
        point_c = item + 3
        point_d = item + 5

        for item_v in value_kvoid:
            if point_a == item_v and not samecolumn(point_a, item):
                possibleLHor.append([item,point_a]);
            if point_b == item_v and not samecolumn(point_a, item):
                possibleLHor.append([item,point_b]);
            if point_c == item_v and not samecolumn(point_a, item):
                possibleLHor.append([item,point_c]);
            if point_d == item_v and not samecolumn(point_a, item):
                possibleLHor.append([item,point_d]);

    ## print  possibleLHor

    for item in possibleLHor:
        item.append(item[0]-1)
        item.append(item[0]+1)

    ## print  possibleLHor 

    markAsVert = []
    achei1S = False
    for item in value_kvoid:
        for x in value_kvoid:
            if x == item + 4:
                achei1S = True
        if achei1S == True:
            achei1S = False
            for y in value_kvoid:
                if y == item -4: 
                    if item >= 5 and item <= 12:
                        markAsVert.append(item)

    ## print markAsVert

    possibleLVert = []
    for item in markAsVert:
        point_a = item - 3
        point_b = item - 5
        point_c = item + 3
        point_d = item + 5

        for item_v in value_kvoid:
            if point_a == item_v and not sameline(point_a,item):
                possibleLVert.append([item,point_a]);
            if point_b == item_v and not sameline(point_b,item):
                possibleLVert.append([item,point_b]);
            if point_c == item_v and not sameline(point_c,item):
                possibleLVert.append([item,point_c]);
            if point_d == item_v and not sameline(point_d,item):
                possibleLVert.append([item,point_d]);
            
    ## print possibleLVert

    for item in possibleLVert:
        item.append(item[0]-4)
        item.append(item[0]+4)

    ## print possibleLVert

    ## print value_kvoid

    return possibleLVert, possibleLHor


def play(origkeys, possibleLV, possibleLH, table_orig, color):

    numeric_table={'a1':1,'b1':2,'c1':3,'d1':4,'a2':5,'b2':6,'c2':7,'d2':8,'a3':9,'b3':10,'c3':11,'d3':12, 'a4':13,'b4':14,'c4':15,'d4':16}
    string_table ={1:'a1',2:'b1',3:'c1',4:'d1',5:'a2',6:'b2',7:'c2',8:'d2',9:'a3',10:'b3',11:'c3',12:'d3', 13:'a4',14:'b4',15:'c4',16:'d4'}
    
    orig_value_blues = []
    for item in origkeys:
        orig_value_blues.append(numeric_table[item])
    

    possibleLVH = possibleLV + possibleLH
    ##print "juntado --> " + str(possibleLV)

    ## testa e remove se tem o L original
    if possibleLVH is not None:
        for item in possibleLVH:
            if len(frozenset(orig_value_blues).intersection(item)) == len(orig_value_blues):
                possibleLVH.remove(item)

    lenghtPVH = len(possibleLVH)
    chooseL = random.randint(0,lenghtPVH-1)
    LinStringFormat = []

    if possibleLVH is not None:
        print possibleLVH[chooseL]
        for item in possibleLVH[chooseL]:            
            table_orig[string_table[item]] = color
    
    return table_orig

def bot(table,color):
    tableClear, originalKeys = tableWithoutBlue(table,color)
    ##dt.draw(tableClear)
    possV, possH = findPossiblesL(tableClear)
    new_table = play(originalKeys, possV, possH, tableClear, color)
    return new_table