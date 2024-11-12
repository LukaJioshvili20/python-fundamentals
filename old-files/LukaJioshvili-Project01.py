choice = input("Enter Encrypt or Decrypt: ").capitalize()

if choice != "Encrypt" and choice != "Decrypt":
    print("Incorrect Input")
    exit()

text = input("Enter Text: ").upper()
key = input("Enter Keyword: ").upper()

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def GenerateTable(alphabet):
    table = ()
    for i in alphabet:
        table += (alphabet,)
        alphabet += i
        alphabet = alphabet[1:]
    return table


def GenerateKey(key):
    key = list(key)
    i = 0
    while len(key) <= len(text):
        key.append(key[i])
        i += 1
    return key


def Encrypt(text, key, table):
    encryptedText = []
    j = 0
    for i in range(0, len(text)):
        if text[i] not in alphabet:
            encryptedText.append(text[i])
        else:
            rowIndex = ord(text[i]) - 65
            columnIndex = ord(key[j]) - 65
            encryptedText.append(table[rowIndex][columnIndex])
            j += 1

    return encryptedText


def Decrypt(text, key, table):
    decryptedText = []
    j = 0
    for i in range(0, len(text)):
        if text[i] not in alphabet:
            decryptedText.append(text[i])
        else:
            rowIndex = (ord(text[i]) - 65) - (ord(key[j]) - 65)
            decryptedText.append(table[rowIndex][0])
            j += 1
    return decryptedText


table = GenerateTable(alphabet)
key = GenerateKey(key)

if choice == "Encrypt":
    encrypt = Encrypt(text, key, table)
    print("Encrypted Result: " + "".join(encrypt))
else:
    decrypt = Decrypt(text, key, table)
    print("Decrypted Result: " + "".join(decrypt))
