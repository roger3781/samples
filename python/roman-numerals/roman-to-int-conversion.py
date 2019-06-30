def romanNumeralHashTable():
    symbols = {
        "M":1000, 
        "CM":900, 
        "D":500, 
        "CD":400,
        "C":100, 
        "XC":90, 
        "L":50, 
        "XL":40,
        "X":10, 
        "IX":9, 
        "V":5, 
        "IV":4,
        "I":1, 
    }
    return symbols

def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
        ]
    
    symbols = romanNumeralHashTable()

    roman_num = ''
    i = 0
    while  num > 0:
        for _ in range(num // symbols[syb[i]]):
            roman_num += syb[i]
            num -= symbols[syb[i]]
        i += 1
    return roman_num
    
 def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    symbols = romanNumeralHashTable()

    num = 0
    index = 0
    while index < len(s):
        char = s[index]
        if index < len(s) - 1:
            doublechar = s[index] + s[index+1]
            if doublechar in symbols:
                num += symbols[doublechar]
                index += 1
            else:
                num += symbols[char]
        else:
            num += symbols[char]
        index += 1
    return num
