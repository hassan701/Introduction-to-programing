def findvalue(mydict, val):
    maps=[]
    for x in sorted(mydict.keys()):
        if val == mydict.get(x): maps.append(x)
    return maps

def main():
    mydict = { 'a' : 0, 'b': 1, 'c' : 2, 'd':1, 'e':1}
    print(findvalue(mydict,val=1))

main()