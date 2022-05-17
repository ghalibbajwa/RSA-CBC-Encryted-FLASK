
from numpy import number

import random

numbers=[0,1,2,3,4,5,6,7,8,9]
# key=[0,1,2,3,4,5,6,7,8,9]
# random.shuffle(key)


def encrypt(message,key):
    n=['1','2','3','4','5','6','7','8','9','0']
    ciphertext=''
    for i in range(len(message)):
        if(message[i] in n):
            if int(message[i]) in numbers:
                ciphertext+=str(key[int(message[i])])
        else:
            ciphertext+=message[i]

    return ciphertext

def decrpyt(ciphertext,numbers,key):
    message=''
    n=['1','2','3','4','5','6','7','8','9','0']

    for i in range(len(ciphertext)):
        if(ciphertext[i] in n):
            for j in range(len(key)):
                if ciphertext[i]==str(key[j]):
                    message+=str(numbers[j])
        else:
            message+=ciphertext[i]
    return message

# msg='[1,23,4,4125,1,42,51,524,2313,421,5132]'
# cyp=encrypt(msg,key)
# print(cyp)

# print(decrpyt(cyp,numbers,key))
