# Runes CRYPTO [70]

Here's challenge:

![](https://raw.githubusercontent.com/ozancetin/CTF-Writeups/master/2019/angstormCTF2019/Runes/runes.png)


Here's given [runes.txt](https://raw.githubusercontent.com/ozancetin/CTF-Writeups/master/2019/angstormCTF2019/Runes/runes.txt)
```
n: 99157116611790833573985267443453374677300242114595736901854871276546481648883
g: 99157116611790833573985267443453374677300242114595736901854871276546481648884
c: 2433283484328067719826123652791700922735828879195114568755579061061723786565164234075183183699826399799223318790711772573290060335232568738641793425546869
```

Its basic paillier crypto challenge.

Here's solution python code

```python
#python2
#theory from https://asecuritysite.com/encryption/pal_ex
# @j3sus

import gmpy #You can use gmpy2 for invert as a gmpy2.invert

n= 99157116611790833573985267443453374677300242114595736901854871276546481648883
g= 99157116611790833573985267443453374677300242114595736901854871276546481648884
c= 2433283484328067719826123652791700922735828879195114568755579061061723786565164234075183183699826399799223318790711772573290060335232568738641793425546869

# n factorization with http://factordb.com/index.php 
p= 319848228152346890121384041219876391791
q= 310013024566643256138761337388255591613

#gLambda = (p-1) * (q-1)

gLambda = 99157116611790833573985267443453374676670380861876746755594725897938349665480

#calculating the value of the L function, and then gMu, which is the inverse of l mod n
l = (pow(g,gLambda,n*n)-1)//n
gMu = gmpy.invert(l,n)

#The public key is then (n,g) and the private key is (gLamda,gMu)
#And is decrypted with:

l = (pow(c, gLambda, n*n)-1) // n
m = (l * gMu) % n

plaintext = str(hex(m))[2::]
print(''.join([chr(int(''.join(c0), 16)) for c0 in zip(plaintext[0::2],plaintext[1::2])]))
```
