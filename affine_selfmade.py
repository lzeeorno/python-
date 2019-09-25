import sys, random

SYMBOLS = ''.join([chr(i) for i in range(ord(' '),ord('~')+1)])

def affine(k1,k2):
    cipher = True
    # x = input("chose cipher(1) or decrypt(2):")
    # x = int(x)
    # if x == 2:
    #     cipher == False
    if cipher == True:
        text = input("Enter the ord(String) to cipher: ")
        text_num = int(text)
        # print(text)
        cipherNum = ((text_num*k1)+k2) % 26
        print("Cipher number is: %d" % cipherNum)
    # else:
    #     text = input("Enter the ord(String) to decrypt: ")
    #     text_num = int(text)
    #     decryptNum = ((text_num-k2)*k1) % 26
    #     print("Decrypt number is %d" % decryptNum)



def find_gcd(a,b):
    while a != 0:
        a, b = b%a, a
    return b
def find_mod():
    a,b = input("Enter the two number such that a mod b: ").split()
    a = int(a)
    b = int(b)
    mod_a = a % b
    print('%d mod %d is: %d' % (a,b,mod_a))
    #let x = mod inverse
    for x in range(1,b):
        if((x*mod_a)%b == 1):
            print('The modular inverse of %d is: %d'% (a,x))
            return x
    return
def main():
    #mode = input("chose mode bu enter either encrypt or decrypt: ")
    #MyMessage = input("""Input the message: """)
    fun = input("chose what do you want to do,"
    "1 for find gcd,"
    "2 for find mod,"
    "3 for affine cipher:  ")
    if int(fun) == 1:
        x,y = input('Enter two num to find gcd: ').split()
        x = int(x)
        y = int(y)
        gcd = find_gcd(x,y)
        print('The gcd of %d and %d is: %d' % (x, y, gcd))
    elif int(fun) == 2:
        find_mod()
    elif int(fun) == 3:
        key1,key2 = input('Enter two keys for affine cipher: ').split()
        k1 = int(key1)
        k2 = int(key2)
        affine(k1,k2)

main()
