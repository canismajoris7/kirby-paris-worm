global cl
cl = []
for i in [char for char in str(input('put in kirby-paris worm'))]:
    cl.append(int(i))

def clprinter(x):
    r1 = ''
    r2 = ''
    r3 = ''
    r4 = ''
    r5 = ''
    for i in x:
        r1 += "              _,.--.  "
        r2 += "      " + str(i) + "     .'`      -"
        r3 += ".'.       .'.'`  '``' "
        r4 += " '.`-...-'.'          "
        r5 += "   `-...-'            "
    print(r1)
    print(r2)
    print(r3)
    print(r4)
    print(r5)
def next(ne):
    global cl
    r = cl[-1]
    del cl[-1]
    print('')
    print('you cut the hydra worms ' + str(r) + ' part off')
    print(clprinter(cl))
    p = len(cl)
    for i in cl:
        p -= 1
        if cl[p] > r:
            t = cl[p:]
            print('the hydra worm regrew ' + str(t) + ' ' + str(ne) + ' times')
            for ele in range(0, ne):
                for i in t:
                    cl.append(i)
            break

print('')
print(clprinter(cl))
ner = 0
while cl != []:
    if input('press enter to attack') == '':
        ner += 1
        next(ner)
        print('')
        print(clprinter(cl))
print('')
print('it took ' + str(ner) + ' steps to kill KIRBY-PARIS`S WORM')
