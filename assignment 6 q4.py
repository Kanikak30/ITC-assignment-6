def Pangram(strg):

    on = ord('a')
    off = ord('z')
    #print(on)
    strg = strg.lower()
    letters = list(map(str,''.join(strg.split())))
    #print(letters)
    for i in range(on, off + 1):
        if  chr(i) in letters: continue
        else: return False
    return True



if(Pangram(input())) : print('Pangram.')
else:print('not a Pangram.')
