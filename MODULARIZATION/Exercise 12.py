def makeForms(verb):
    ends= ('o','ch','s','sh','x','z')
    newverb = "what"
    if(verb.endswith('y')== True):
        newverb= verb[:-1]+'ies'
    elif(verb.endswith(ends) == True):
        newverb = verb + 'es'
    else:
        newverb=verb+'s'
    return newverb
def main():
    print(makeForms("try"),makeForms("brush"),makeForms("run"),makeForms("fix"))

main()