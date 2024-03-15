from Crypto.Util.number import *
from sage.all import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from hashlib import sha256
p = 0xdd6cc28d
g = 0x83e21c05
A = 0xcfabb6dd
B = 0xc4a21ba9
b=1913706799
ciphertext = b'\x94\x99\x01\xd1\xad\x95\xe0\x13\xb3\xacZj{\x97|z\x1a(&\xe8\x01\xe4Y\x08\xc4\xbeN\xcd\xb2*\xe6{'
'''
Sagemath part 

R = IntegerModRing(p)
b = discrete_log(R(B), R(g))

print(b)
1913706799
'''
shared_secret=pow(A,b,p)
hash = sha256()
hash.update(long_to_bytes(shared_secret))
key = hash.digest()[:16]
iv = b'\xc1V2\xe7\xed\xc7@8\xf9\\\xef\x80\xd7\x80L*'
cipher = AES.new(key, AES.MODE_CBC, iv)
ciphertext = b'\x94\x99\x01\xd1\xad\x95\xe0\x13\xb3\xacZj{\x97|z\x1a(&\xe8\x01\xe4Y\x08\xc4\xbeN\xcd\xb2*\xe6{'

flag = cipher.decrypt(ciphertext)
print(flag)