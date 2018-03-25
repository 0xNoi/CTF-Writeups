#python2 script @Ozan

import binascii
filename = 'flag.png.crypt'
with open(filename, 'rb') as f:
    content = f.read()
XORdata = binascii.hexlify(content)

cipher = (XORdata).decode('hex')

for i in range(0x00,0xff):
	result = ""
	for j in cipher:
		result += chr(i^ord(j))
	if 'PNG' in result:
		solved = open("flag.png","w")
		solved.write(result)
		solved.close()
