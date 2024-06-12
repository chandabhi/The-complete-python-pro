alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction = input("Type 'encode' for encryption , type 'decode' for decryption : \n")
text = input("Type the message : \n").lower()
shift = int(input("Type the shift number : \n"))
words = text.split()
length = len(words)
def encrypt():
    enMsg = ''
    for i in range(len(words)):
        for j in range (len(words[i])):
            findIndex = alphabet.index(words[i][j])
            shiftindex = findIndex+shift
            if(shiftindex > (len(alphabet)-1)):
                newIndex = shiftindex - (len(alphabet)-1)
                enMsg += alphabet[newIndex-1] 
            else :
                enMsg += alphabet[findIndex+shift]
        enMsg += " "
    print(enMsg)

def decrypt():
    deMsg = ''
    for i in range(len(words)):
        for j in range (len(words[i])):
            findIndex = alphabet.index(words[i][j])
            shiftindex = findIndex - shift 
            if(shiftindex <0):
                deMsg += alphabet[shiftindex] 
            else :
                deMsg += alphabet[findIndex-shift]
        deMsg += " "
    print(deMsg)

if direction == 'encode':
    encrypt()
elif direction == 'decode':
    decrypt()
