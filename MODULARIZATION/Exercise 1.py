def listntuple(x):
    y=[]
    y=x.split(",")
    return print("List :",y,"\ntuple :",tuple(y))



def main():
    y= (input("Put in a sequence of numbers separated by a comma:"))
    listntuple(y)

main()