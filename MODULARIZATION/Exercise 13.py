def makeForming(verb):
    newverb = "what"
    end = ("flee","agree","be","believe","deserve","desire","dislike","forgive","hate","have","hope","imagine","include","intend","involve","know","lack","like","love","matter","mean","measure","notice"'"owe"'"perceive","please","presuppose","realize","recognize","require","resemble","see","suffice","suppose","surprise","taste","think","value","weigh","wish")

    if verb.endswith('e')== True and verb not in end and verb[-2] != 'i':
        newverb= verb[:-1]+'ing'

    elif(verb.endswith('ie') == True):
        newverb = verb[:-2] + 'ing'

    elif len(verb) > 2  and verb[-3] not in 'aeiou' and verb[-2] in 'aeiou' and verb[-1] not in 'aeiou':
        newverb = verb +verb[-1] + 'ing'
    else:
        newverb=verb+'ing'
    return newverb
def main():
    print(makeForming("hug"),makeForming("be"),makeForming("see"),makeForming("lie"),makeForming("move"))

main()
