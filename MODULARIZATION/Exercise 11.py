def char_freq(string):
    all_freq = {}
    for i in string:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1

    return all_freq

def main():
    a= "How many are there I wonder"
    print(char_freq(a))

main()