def decodeMorse(morseCode):
    morseCode = '  ... '
    print morseCode
    while morseCode[0] == ' ':
        morseCode = remove_prefix(morseCode, ' ')
        print morseCode
    print morseCode[len(morseCode)-1]
    print len(morseCode)
    while morseCode[len(morseCode)-1] == ' ':
        morseCode = remove_suffix(morseCode, ' ')
        print morseCode

    lst2 = []
    morseCode = morseCode.replace('   ',' # ')   #Replaces "   " with " # "
    MORSE_CODE["#"] = "#"                        #adding a new value(#) to the MORSE_CODE dictionary
    lst1 = morseCode.split()
    for x in lst1: lst2.append(MORSE_CODE[x])
    decoded = ''.join(lst2)
    return decoded.replace('#',' ')


def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text

def remove_suffix(text, suffix):
    if text.endswith(suffix):
        return text[:len(suffix)]
    return text
