def find_longest_word(lwords):
    b=[]
    for i in lwords:
       b.append(len(i))
    return max(b)
    #return lwords[b.index(max(len(b))] #if you want to return the word but it only returns 1 if ther are multible

def main():
    a=['There','are','a','lot','of','words']
    print(find_longest_word(a))

main()