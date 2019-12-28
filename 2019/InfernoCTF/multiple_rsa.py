import gmpy

'''
Challenge
---------------
e = 65537
N = 25693197123978473
enc_flag = ['0x2135d36aa0c278', '0x3e8f43212dafd7', '0x7a240c1672358', '0x37677cfb281b26', '0x26f90fe5a4bed0', '0xb0e1c482daf4', '0x59c069723a4e4b', '0x8cec977d4159']
Help me find out the secret to decrypt the flag
'''
#using with http://www.factordb.com/index.php for quick factorization for n = 25693197123978473

p = 150758089
q = 170426657
e = 65537
n = p*q
ciphertexts = [9347856374743672,17608967038283735,2148723843343192,15594910206401318,10969895787609808,194483711040244,25262832047771211,154947781738841]
phi = (p - 1) * (q - 1)
d = gmpy.invert(e,phi) 


result =[]
for ct in ciphertexts:
	pt = pow(ct,d,n)
	pt = str(hex(pow(ct, d, n)))[2::]
	result2 = ''.join([chr(int(''.join(c), 16)) for c in zip(pt[0::2],pt[1::2])])
	result.append(result2)
result_final = ''.join(result)

print result_final
