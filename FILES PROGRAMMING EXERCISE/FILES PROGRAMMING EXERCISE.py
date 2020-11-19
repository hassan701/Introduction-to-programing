def word_count(text):
    mydict = {}
    hapax = []
    key = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p','q', 'r', 's', 't', 'u', 'v','w','x', 'y' , 'z']
    for x in range(len(text)):
        word = ''
        for i in text[x]:
            if i in key:
                word = word + i
        mydict[word] = mydict.get(word, 0) + 1
    for wo,nu in mydict.items():
        if nu == 1:
            hapax.append(wo)
    return hapax
def main():
    file = open('pg63807.txt', encoding='utf8')# The Great Green Blight
    text = file.read().lower().replace('\n', ' ').split(' ')
    #print(text)
    print(word_count(text))

main()












#punctuation ={"'","!",'"','#','$','%','&','(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','[',']','^','_','`','{','|','}','~'}
