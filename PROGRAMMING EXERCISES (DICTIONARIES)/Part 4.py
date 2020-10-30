def wordfrequencies(mylist):
    freq = {}
    for i in mylist:
        freq[i] = freq.get(i, 0) + 1
    return freq

def main():
    mylist= "How many are there I wonder are there".split(" ")
    print(wordfrequencies(mylist))

main()