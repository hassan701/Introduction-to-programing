def pangram(text):
    i = 'abcdefghijklmnopqrstuvwxyz'
    q= False
    for char in i:
        if char in text:
            q = True
        else:
            return False

    return q

def main():
    a = "the quick brown fox jumps over the lazy dog"
    print(a)
    print("Is it a Pangram:", pangram(a))

main()