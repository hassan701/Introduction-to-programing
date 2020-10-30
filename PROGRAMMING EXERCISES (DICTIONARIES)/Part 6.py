def decoder(message):
    key = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't', 'h': 'u', 'i': 'v', 'j': 'w', 'k': 'x',
           'l': 'y', 'm': 'z', 'n': 'a', 'o': 'b', 'p': 'c', 'q': 'd', 'r': 'e', 's': 'f', 't': 'g', 'u': 'h', 'v': 'i',
           'w': 'j', 'x': 'k', 'y': 'l', 'z': 'm', 'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R', 'F': 'S', 'G': 'T',
           'H': 'U', 'I': 'V', 'J': 'W', 'K': 'X', 'L': 'Y', 'M': 'Z', 'N': 'A', 'O': 'B', 'P': 'C', 'Q': 'D', 'R': 'E',
           'S': 'F', 'T': 'G', 'U': 'H', 'V': 'I', 'W': 'J', 'X': 'K', 'Y': 'L', 'Z': 'M'}
    truem=''
    for x in range(len(message)):
        for i in message[x]:
            if i in sorted(key.keys()):
                truem = truem + str(key.get(i))
            else:
                truem = truem + i
        truem= truem + " "

    return truem

def main():
    message= "Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"
    hmm= "Caesar cipher, I hardy know her!"
    print(decoder(message.split()))
    print(decoder(hmm.split()))

main()