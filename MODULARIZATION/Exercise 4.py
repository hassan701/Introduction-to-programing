def s_member(x,a=[]):
    for i in range(len(a)):
        if x == a[i]:
            return True
    return False

def main():
    x = 1
    a = [1,1,2,3,4,4,5,6,7]
    print(s_member(x,a))

main()