from Crypto.Cipher import AES

a="dd15d5edb5a240a7c8f760ac86f0fca9"
b=[]
for x in range(0,len(a),2):
    b.append(int("0x"+a[x:x+2],16))
b=str(bytearray(b))
for key_b1 in range(256):
    for key_b2 in range(256):
        decipher = AES.new(str(bytearray([key_b1,key_b2])*8), AES.MODE_ECB)
        if decipher.decrypt(b)=="a"*16:
            print(bytearray([key_b1,key_b2]))
            break
decipher = AES.new("fL"*8, AES.MODE_ECB)
m=decipher.encrypt("BnMb7wu7tD3wYAYv")
print(m.encode("hex"))