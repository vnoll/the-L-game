from colorama import init, Fore
init()


def draw(table):
    line = []
    line = [[table["a4"],table["b4"],table["c4"],table["d4"]], [table["a3"],table["b3"],table["c3"],table["d3"]], [table["a2"],table["b2"],table["c2"],table["d2"]], [table["a1"],table["b1"],table["c1"],table["d1"]]]
    
    for x in line:
        printList = ""
        for i in x:
            if i == "void":
                printList += Fore.WHITE + "#########"
            if i == "neutral":
                printList += Fore.YELLOW + "#########"
            if i == "red":
                printList += Fore.RED + "#########"
            if i == "blue":
                printList += Fore.BLUE + "#########"
    
        print printList
        print printList
        print printList
        print printList
        
    


    




