def order(strg):
    if '-' not in strg or ' ' in strg:
        print('Enter a valid value.')
        return 
    strg = strg.split('-')
    strg.sort()
    print('-'.join(map(str,strg)))

order(input('Enter string: '))
