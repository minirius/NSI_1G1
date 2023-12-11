def inverse(string):
    liste = []
    for i in string:
        liste.insert(0, i)
    return "".join(liste)

def isPalindrome(string):
    return string.lower() == inverse(string.lower())

print(inverse("sikaztnareN suiraM"))
print(isPalindrome("laval"))