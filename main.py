import blueBot as b
import redBot as r
import drawTable as d

v = "void"
n = "neutral"
r = "red"
b = "blue"

table = {"a4":n,"b4":b,"c4":b,"d4":v,"a3":v,"b3":r,"c3":b,"d3":v,"a2":v,"b2":r,"c2":b,"d2":v,"a1":v,"b1":r,"c1":r,"d1":n}

def run():
    print("Running")
    d.draw(table)
    pass

if __name__ == '__main__':
    run()
