def countletterss(a=[]):
    b=[]
    for i in range(len(a)):
        b.append(len(a[i]))
    return b

def main():
    a=['There','are','a','lot','of','words']
    print(countletterss(a))

main()