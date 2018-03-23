# XOR

Here's the challenge:
![](https://raw.githubusercontent.com/ozancetin/CTF-Writeups/master/2018/angstromCTF2018/XOR/1.png)

```
fbf9eefce1f2f5eaffc5e3f5efc5efe9fffec5fbc5e9f9e8f3eaeee7
```

Its very basic xor challenge, it must be single byte xor cipher and write a quick bruteforce python2 script

Here's the script:

``` python
cipher = 'fbf9eefce1f2f5eaffc5e3f5efc5efe9fffec5fbc5e9f9e8f3eaeee7'.decode('hex')

for i in range(0x00,0xff):
	result = ''
	for j in cipher:
		result += chr(i^ord(j))
	if 'actf{' in result:
		print 'flag :', result
```

So flag must be:

```
actf{hope_you_used_a_script}
```



