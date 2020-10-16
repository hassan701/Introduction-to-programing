def filter_longest_words(lwords,n):
    b=[]
    for i in lwords:
        if len(i) > n:
            b.append(i)
    return b


def main():
    a=['There','are','a','lot','of','words']
    print(filter_longest_words(a,3))

main()