# readyXORnot

```
Challenge: 
original data: "El Psy Congroo"
encrypted data: "IFhiPhZNYi0KWiUcCls="
encrypted flag: "I3gDKVh1Lh4EVyMDBFo="

The flag is not in the traditional gigem{flag} format.
```

Here's the python 2 script

```python
import base64

ori = 'El Psy Congroo'
enc = base64.b64decode('IFhiPhZNYi0KWiUcCls=')
flag = base64.b64decode('I3gDKVh1Lh4EVyMDBFo=')
dec = ''
for i, c in enumerate(enc):
  key = ord(c) ^ ord(ori[i])
  dec += chr(ord(flag[i]) ^ key)
  
print dec
```

So flag is
```
FLAG: Alpacaman
```
