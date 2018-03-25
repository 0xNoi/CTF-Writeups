# looser
Here's the challenge:
![](https://raw.githubusercontent.com/ozancetin/CTF-Writeups/master/2018/Securinets%20CTF%20Quals%202018/looser/1.png)

[flag.png.crypt](https://github.com/ozancetin/CTF-Writeups/blob/master/2018/Securinets%20CTF%20Quals%202018/looser/flag.png.crypt?raw=true)

I thought it can be single byte xor and I write a clear python2 script:

```python

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
```

It worked and here's the flag.png

![](https://raw.githubusercontent.com/ozancetin/CTF-Writeups/master/2018/Securinets%20CTF%20Quals%202018/looser/flag.png)
