def toList(text):
    textL = []
    for i in text:
        textL.append(i)
    return textL

def checkSame(text, lt, ls):
    textL = toList(text)
    c = 0
    noDummy = False
    while c < lt:
        fragment = text[c:(c+ls)]
        if c+ls <= lt and fragment == substr:
            noDummy = True
            textL.insert(c, "[")
            textL.insert(c+ls+1, "]")
            text = ''.join(textL)
            lt += 2
            c += ls+2
        else:
            c += 1
    if noDummy == True:
        print(''.join(textL))
    return noDummy

def checkDummy(text, lt, ls):
    textL = toList(text)
    c = 0
    ss = 0
    dummy = 0
    while c < lt:
        diff = 0  
        ss = 0  
        while ss < ls and c+ss < lt:
            if text[c+ss] != substr[ss]:
                diff += 1
                dummy = c+ss
            ss += 1
        
        if diff == 1 and c != lt-1: 
            textL[dummy] = '?'
            textL.insert(c, "[")
            textL.insert(c+ls+1, "]")
            text = ''.join(textL)
            lt += 2
            c += ls+2
        else:
            c += 1
    print(''.join(textL))

text = input("Text: ")
substr = input("Substring: ")
lt = len(text)
ls = len(substr)

if checkSame(text, lt, ls) == True:
    pass
else:
    checkDummy(text, lt, ls)
