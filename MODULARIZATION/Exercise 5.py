def s_member(x,a=[]):
    for i in range(len(a)):
        if x == a[i]:
            return True
    return False

def overlapping(lst1,lst2):
    for i in lst1:
        for b in lst2:
            a = s_member(i,lst2)
            if a == True:
                return True
    return False

def main():
    lst1= [2,2,3,4,5,5]
    lst2= [1,6,7,8,7]
    print(overlapping(lst1,lst2))

main()

