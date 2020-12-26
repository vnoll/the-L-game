import blueBot as bB
import redBot as rB
import drawTable as d
import time
import copy

v = "void"
n = "neutral"
r = "red"
b = "blue"

def run():
    table = {"a4":n,"b4":b,"c4":b,"d4":v,"a3":v,"b3":r,"c3":b,"d3":v,"a2":v,"b2":r,"c2":b,"d2":v,"a1":v,"b1":r,"c1":r,"d1":n}
    print("Running ...")
    d.draw(table)
    cpy = copy.deepcopy(table)
    while True:
        print("BLUE player running ..")
        table_botBlue = bB.bot(table,"blue")
        time.sleep(2)
        d.draw(table_botBlue)
        if cpy == table_botBlue:
            print "Winner is RED"
            break

        cpy = copy.deepcopy(table_botBlue)      

        print("RED player running ..")
        table_botRed = bB.bot(table, "red")
        time.sleep(2)
        d.draw(table_botRed)
        if cpy == table_botRed:
            print "Winner is BLUE"
            break      
        cpy = copy.deepcopy(table_botRed) 

if __name__ == '__main__':
    run()