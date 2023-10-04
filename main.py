#Run the programme, input prime number p and q, then the message, the result will be in the console output

import math
prime=[17,13,503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, \
       601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, \
       701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, \
       809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, \
       907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
def computeGCD(x, y):
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small + 1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i
    return gcd

def RSAgen(p, q):
    n = p*q
    #Calculating n
    z = (p-1)*(q-1)
    #Calculating z

    e=2
    while(e<z):
        # e is co-prime to z and smaller than z, thus the GCD between e and z is 1
        if(computeGCD(e, z) == 1):
            break
        else:
            e = e+1
    #print("encryption key e=",e)

    k = 1
    while True:
        #Calculate coefficient K that satisfy ed-1=kz (which is same as ed-1 mod z = 0)
        #ed-1=kz thus d=(1+kz)/e. z and e is known, and d is integer
        di = int((1 + (k*z))/e)
        df = (1 + (k*z))/e
        if di == df:
            break
        else:
            k = k+1
    d=di
    #print("decryption key d=",d)
    return(n,z,e,d)

def RSAe(msg, e, n):
    #RSA encryption using m e and n
    me = pow(msg,e)
    c = me % n
    return(c,me)
    #print("Encrypted data = ", c)

def RSAd(c, d, n):
    #RSA decryption using m d and n
    m = pow(c, d, n)
    return(m)
    #print("Decrypted Message = ", m)
p=0
q=0
while not(p in prime):
    p=int(input("Input prime number P between 500-1000: \n"))
    if not(p in prime):
        print("Please enter a prime number between 500-1000")
while not(q in prime):
    q=int(input("Input prime number Q between 500-1000: \n"))
    if not(q in prime):
        print("Please enter a prime number between 500-1000")
n,z,e,d=RSAgen(p,q)
print("n=",n)
print("z=",z)
print("encryption key e=",e)
print("decryption key d=",d)

msgs=input("Input message: \n")

msgn=[]
j=0
for j in range(len(msgs)):
    #Transform the message from character to numerical
    num=ord(msgs[j])-64
    if ((num>0 and num<=58)):
        msgn.append(num)
    j=j+1
print("The numerical representation of the message is:",msgn)

#Encryption
msgc=[]
msgme=[]
k=0
for k in range(len(msgn)):
    msgc.append(RSAe(msgn[k],e,n)[0])
    msgme.append(RSAe(msgn[k],e,n)[1])
    k=k+1
print("The m^e of each character is:",msgme)
print("The ciphertext of each character is:",msgc)

#Decryption
msgdn=[]
k=0
for k in range(len(msgc)):
    msgdn.append(RSAd(msgc[k],d,n))
    k=k+1
#print(msgdn)

#Transform back to ASCII form
msgds=[]
k=0
for k in range(len(msgdn)):
    msgds.append(chr(msgdn[k]+64))
    k=k+1
print("The decoded message is:",''.join(msgds))