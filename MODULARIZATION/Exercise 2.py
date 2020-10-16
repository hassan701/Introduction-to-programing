def translate(text):
    i = []
    for char in text:
        if char in 'aeiou':
            i.append(char)
        elif char == ' ':
            i.append(' ')
        else:
            i.append(char)
            i.append('o')
            i.append(char)
    return print(''.join(i))


def main():
    text=input("Please put in your text:")
    translate(text)

main()