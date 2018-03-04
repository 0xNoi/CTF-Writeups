#Python 2 Script

import base64

ori = 'El Psy Congroo'
enc = base64.b64decode('IFhiPhZNYi0KWiUcCls=')
flag = base64.b64decode('I3gDKVh1Lh4EVyMDBFo=')
dec = ''
for i, c in enumerate(enc):
  key = ord(c) ^ ord(ori[i])
  dec += chr(ord(flag[i]) ^ key)
  
print dec

