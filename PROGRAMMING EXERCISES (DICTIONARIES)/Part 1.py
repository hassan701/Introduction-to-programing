def removekeys(mydict, keylist):
    for x in sorted(mydict.keys()):
        if x in keylist: mydict.pop(x)
    return mydict
def main():
    mydict = { 'a' : 0, 'b': 1, 'c' : 2}
    keylist = ['a','c']
    print(removekeys(mydict,keylist))

main()