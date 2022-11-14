# New String
def solve(alphabet, n, strings, k):
    normalAlphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypt = {}
    decrypt = {}
    for i in range(len(alphabet)):
        encrypt[normalAlphabet[i]] = alphabet[i]
        decrypt[alphabet[i]] = normalAlphabet[i]
    
    
    encryptedStrings = []
    for string in strings:
        encryptedString = ""
        for letter in string:
            encryptedString += encrypt[letter]
        encryptedStrings.append(encryptedString)
    
    encryptedStrings.sort()
    print(encryptedStrings)
    
    target = encryptedStrings[k - 1]
    print(target)
    decryptedString = ""
    for letter in target:
        decryptedString += decrypt[letter]
    return decryptedString

def main():
    alphabet = input()
    n = int(input())
    strings = []
    for i in range(n):
        string = input()
        strings.append(string)
    k = int(input())
    
    print(solve(alphabet, n, strings, k))
        

if __name__ == "__main__":
    main()