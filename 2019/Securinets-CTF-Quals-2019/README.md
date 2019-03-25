# Securinets CTF Quals 2019

Here's the challenge: 
![](https://raw.githubusercontent.com/ozancetin/CTF-Writeups/master/2019/Securinets-CTF-Quals-2019/MAZE/MAZE.png)

Here's the given zip
[chall.zip](https://github.com/ozancetin/CTF-Writeups/blob/master/2019/Securinets-CTF-Quals-2019/MAZE/chall.zip?raw=true)

Inside the zip, there are 101 public key and 1 ciphertext as a decimal format and we need to find correct public key and try to crack if it is possible then create private key for decrypt the ciphertext.

First of all I thought a write script but there are already tool [RsaCtfTool](https://github.com/Ganapati/RsaCtfTool)

This parameter usefull for multiple public key

```python2 RsaCtfTool.py --publickey "*.pem" --private
```
![](https://raw.githubusercontent.com/ozancetin/CTF-Writeups/master/2019/Securinets-CTF-Quals-2019/MAZE/rsactftool.png)

after a bit waiting I saw only 2 key breakable as a  :
![](https://raw.githubusercontent.com/ozancetin/CTF-Writeups/master/2019/Securinets-CTF-Quals-2019/MAZE/private1.key)
![](https://raw.githubusercontent.com/ozancetin/CTF-Writeups/master/2019/Securinets-CTF-Quals-2019/MAZE/private2.key)

So thats easy, we dont need to write a any script for 2 private keys.

remember RSA decrypting rule 
```To decrypt a ciphertext c, compute c^d mod (N)```
N : Modulus
d : Private exponent
c : Ciphertext (we already have it)

So we need to find N and d from private key lets do it with openssl thats parameters show us everything about private key

```openssl rsa -text -in private1.key```

output :

```
RSA Private-Key: (2048 bit, 2 primes)
modulus:
    00:b8:42:a7:7d:fb:1d:21:a8:0e:4a:38:79:3e:72:
    d6:05:5f:1a:79:38:1a:bb:6e:88:8e:47:e3:72:1d:
    4f:57:92:7a:a0:f2:df:08:22:e4:8c:a1:ef:2a:63:
    ef:a3:e0:36:6b:7b:46:54:8f:2c:7b:ab:ff:c8:34:
    f3:4b:36:97:98:bf:5c:84:51:58:8e:77:77:8a:32:
    54:68:54:3a:12:42:0b:b1:80:66:16:ce:cf:f3:c4:
    e2:5d:f8:cc:e5:dd:bd:5b:1a:84:d7:53:a8:9f:7c:
    b4:ea:34:79:d8:0c:e9:81:79:e5:9e:9a:cf:85:77:
    30:13:2d:57:d1:d1:f7:71:75:71:e8:3d:df:f6:a8:
    e8:ed:b0:fc:6c:33:2e:5d:d8:0a:5f:01:9a:a4:71:
    3d:49:dd:a7:96:74:5d:d6:7d:f9:b1:8c:c3:11:d7:
    e8:11:d4:0d:16:0f:da:5c:3f:bb:5e:f3:6a:c2:41:
    60:49:7d:41:ab:48:69:06:02:dd:eb:56:18:db:04:
    40:21:75:52:9f:9f:59:eb:58:6f:40:d8:36:02:56:
    44:49:3d:f5:63:6f:23:2c:ac:3f:04:24:76:a9:0f:
    ea:06:3a:dc:31:66:15:c0:b4:79:2c:b1:f9:b6:9f:
    f7:22:80:16:1e:01:c7:68:81:f4:d2:65:97:c3:22:
    53:f5
publicExponent: 65537 (0x10001)
privateExponent:
    00:84:1f:7f:5c:6d:80:a1:0e:91:58:95:10:13:40:
    62:c8:ad:3e:1d:67:a6:7b:79:b1:bf:5c:3a:f2:2b:
    a4:25:e6:29:ba:59:0c:a6:17:e7:0c:14:5d:9b:66:
    d7:82:09:96:dc:11:24:08:24:35:c0:64:3f:df:be:
    60:2a:31:76:18:98:36:ed:c6:2a:9a:d5:7d:49:01:
    f7:d6:6b:76:cc:7a:c1:49:c1:08:f3:17:ce:b3:3c:
    1d:19:46:fb:1d:64:97:8f:c8:ff:32:2b:91:c0:f2:
    ba:03:2a:27:a8:4c:f1:ee:de:8a:50:e5:2f:22:c3:
    a9:1c:47:2a:2e:90:c1:3e:7f:c0:62:3f:e9:45:8b:
    ba:11:c6:ef:34:d1:7e:e0:95:ea:5e:cf:5d:4e:40:
    43:bd:9b:a6:82:12:9f:ef:79:ce:d2:79:9d:cc:89:
    fa:23:a8:9f:90:f4:ce:7c:eb:a0:73:d9:6c:38:eb:
    80:1b:75:b9:4f:4f:91:ee:47:02:6b:ca:80:2e:1e:
    70:ad:4f:f2:2b:96:56:22:da:8a:1a:aa:85:66:6e:
    61:67:ef:35:ec:5f:d0:d9:f9:25:63:2c:68:18:00:
    1e:b8:d2:c9:eb:50:12:c5:90:ce:2e:fd:f6:77:e5:
    ab:22:3f:31:7d:6e:ac:9a:3e:8d:23:f9:33:09:e8:
    8f:4d
prime1:
    00:f0:49:e8:30:d7:29:72:dc:e5:94:e3:86:f7:dc:
    d8:4d:05:7a:97:91:d4:f5:7a:96:3d:8e:61:9a:94:
    d8:34:e2:60:cb:77:e3:d0:d5:38:6b:23:37:91:14:
    4f:50:ff:28:df:38:44:4f:a8:b7:1e:52:d8:31:3c:
    79:da:d9:09:d5:b8:7f:7a:f8:72:f8:f2:22:50:10:
    c7:3a:ca:e0:e1:db:96:b8:8e:0d:e1:5c:ef:6b:58:
    c6:51:b1:a2:61:7e:14:19:c4:51:0e:3c:50:26:21:
    f8:47:70:e0:f7:95:8b:f0:f8:97:c6:83:af:0b:a9:
    0a:30:82:44:fd:42:22:d1:33
prime2:
    00:c4:4e:e9:88:fb:54:c6:96:ee:67:cd:5a:3b:bb:
    b1:59:40:4e:6d:4c:45:3a:43:1c:0c:ed:82:8d:a3:
    f2:1e:fa:0a:c8:c4:70:d0:d6:d2:09:69:7f:58:92:
    ef:95:e0:54:16:10:8e:a1:72:a0:cb:bf:5f:2d:2b:
    b0:d4:8e:2a:93:06:b8:b4:13:eb:05:5e:0f:33:1b:
    89:8b:b9:a0:aa:e9:10:e6:c6:8a:f0:9a:0d:f7:10:
    99:da:c1:4c:29:22:fc:41:9b:3d:97:1e:fe:88:57:
    31:9f:e1:53:f4:a8:73:69:67:48:b5:40:83:48:4a:
    a0:5f:0e:23:73:db:9f:16:37
exponent1:
    00:ef:26:ef:d4:a4:61:19:74:27:7f:9f:50:b6:a2:
    f4:18:fc:69:fe:2e:e3:c0:8a:88:bb:ad:59:11:6c:
    31:1f:b9:6b:d3:36:78:e4:61:42:ac:c7:39:47:c8:
    ea:04:58:60:8a:82:4a:e2:e9:ad:8f:9d:ae:94:9a:
    77:41:4c:a0:90:38:f7:90:21:74:f4:b6:b1:55:f4:
    cd:05:83:e4:7c:86:7c:25:25:25:45:76:a4:c7:b7:
    6c:72:e4:94:13:ea:53:01:2e:35:ea:30:37:29:2c:
    c8:19:fa:8b:bd:7e:f6:f0:17:cb:9f:85:72:93:ed:
    63:39:d2:7d:ed:7e:84:7e:a7
exponent2:
    01:16:5a:ce:ca:6d:96:c8:01:3c:0b:f4:22:fe:90:
    25:e9:68:45:cc:b5:59:74:43:b4:82:a0:45:7e:91:
    f9:bf:f2:cd:57:e1:34:16:ec:84:e6:d3:b0:be:e7:
    9a:d1:ea:45:51:04:29:3a:c4:4f:3c:99:1f:5b:ed:
    97:cf:cd:c6:90:b3:f7:33:61:0a:df:91:7f:fb:f8:
    10:11:10:25:c2:32:b8:c4:82:c2:80:67:f1:65:63:
    24:c6:0b:50:f3:03:a8:ad:5e:72:f6:d5:fc:15:57:
    8e:06:26:7b:e5:6e:f6:37:7f:3c:99:c5:e0:61:a1:
    6f:c5:59:46:ec:01:7e:93
coefficient:
    00:8c:2d:91:12:87:23:5f:b5:9b:ce:ce:94:a1:8c:
    0c:5b:0b:2d:f5:a9:81:6d:f1:ea:f1:bd:d2:2f:80:
    d6:bd:03:a7:b2:7e:e4:7e:0e:dd:f6:3a:ec:9f:ae:
    c2:e7:ec:87:c1:1e:65:76:df:b5:31:3d:64:da:8a:
    98:64:1d:d1:33:75:34:4e:5e:1a:12:26:fa:c6:ce:
    49:b7:6c:49:37:c4:50:01:06:3c:f5:f5:81:37:a1:
    28:ef:26:d3:63:2c:37:24:8f:88:66:54:ce:e0:f7:
    c8:b7:25:61:53:d6:67:16:0e:78:b0:43:8e:9f:fe:
    23:5b:e9:94:c2:bb:77:b0:93
writing RSA key
```

And as you can see here's modulus and private key 

```
modulus:
    00:b8:42:a7:7d:fb:1d:21:a8:0e:4a:38:79:3e:72:
    d6:05:5f:1a:79:38:1a:bb:6e:88:8e:47:e3:72:1d:
    4f:57:92:7a:a0:f2:df:08:22:e4:8c:a1:ef:2a:63:
    ef:a3:e0:36:6b:7b:46:54:8f:2c:7b:ab:ff:c8:34:
    f3:4b:36:97:98:bf:5c:84:51:58:8e:77:77:8a:32:
    54:68:54:3a:12:42:0b:b1:80:66:16:ce:cf:f3:c4:
    e2:5d:f8:cc:e5:dd:bd:5b:1a:84:d7:53:a8:9f:7c:
    b4:ea:34:79:d8:0c:e9:81:79:e5:9e:9a:cf:85:77:
    30:13:2d:57:d1:d1:f7:71:75:71:e8:3d:df:f6:a8:
    e8:ed:b0:fc:6c:33:2e:5d:d8:0a:5f:01:9a:a4:71:
    3d:49:dd:a7:96:74:5d:d6:7d:f9:b1:8c:c3:11:d7:
    e8:11:d4:0d:16:0f:da:5c:3f:bb:5e:f3:6a:c2:41:
    60:49:7d:41:ab:48:69:06:02:dd:eb:56:18:db:04:
    40:21:75:52:9f:9f:59:eb:58:6f:40:d8:36:02:56:
    44:49:3d:f5:63:6f:23:2c:ac:3f:04:24:76:a9:0f:
    ea:06:3a:dc:31:66:15:c0:b4:79:2c:b1:f9:b6:9f:
    f7:22:80:16:1e:01:c7:68:81:f4:d2:65:97:c3:22:
    53:f5
privateExponent:
    00:84:1f:7f:5c:6d:80:a1:0e:91:58:95:10:13:40:
    62:c8:ad:3e:1d:67:a6:7b:79:b1:bf:5c:3a:f2:2b:
    a4:25:e6:29:ba:59:0c:a6:17:e7:0c:14:5d:9b:66:
    d7:82:09:96:dc:11:24:08:24:35:c0:64:3f:df:be:
    60:2a:31:76:18:98:36:ed:c6:2a:9a:d5:7d:49:01:
    f7:d6:6b:76:cc:7a:c1:49:c1:08:f3:17:ce:b3:3c:
    1d:19:46:fb:1d:64:97:8f:c8:ff:32:2b:91:c0:f2:
    ba:03:2a:27:a8:4c:f1:ee:de:8a:50:e5:2f:22:c3:
    a9:1c:47:2a:2e:90:c1:3e:7f:c0:62:3f:e9:45:8b:
    ba:11:c6:ef:34:d1:7e:e0:95:ea:5e:cf:5d:4e:40:
    43:bd:9b:a6:82:12:9f:ef:79:ce:d2:79:9d:cc:89:
    fa:23:a8:9f:90:f4:ce:7c:eb:a0:73:d9:6c:38:eb:
    80:1b:75:b9:4f:4f:91:ee:47:02:6b:ca:80:2e:1e:
    70:ad:4f:f2:2b:96:56:22:da:8a:1a:aa:85:66:6e:
    61:67:ef:35:ec:5f:d0:d9:f9:25:63:2c:68:18:00:
    1e:b8:d2:c9:eb:50:12:c5:90:ce:2e:fd:f6:77:e5:
    ab:22:3f:31:7d:6e:ac:9a:3e:8d:23:f9:33:09:e8:
    8f:4d
    ```
    
    Now we have N and d just convert hex to decimal and pow 
    
    ```python2 
    
    n = int("00b842a77dfb1d21a80e4a38793e72d6055f1a79381abb6e888e47e3721d4f57927aa0f2df0822e48ca1ef2a63efa3e0366b7b46548f2c7babffc834f34b369798bf5c8451588e77778a325468543a12420bb1806616cecff3c4e25df8cce5ddbd5b1a84d753a89f7cb4ea3479d80ce98179e59e9acf857730132d57d1d1f7717571e83ddff6a8e8edb0fc6c332e5dd80a5f019aa4713d49dda796745dd67df9b18cc311d7e811d40d160fda5c3fbb5ef36ac24160497d41ab48690602ddeb5618db04402175529f9f59eb586f40d836025644493df5636f232cac3f042476a90fea063adc316615c0b4792cb1f9b69ff72280161e01c76881f4d26597c32253f5",16)

d = int("00841f7f5c6d80a10e91589510134062c8ad3e1d67a67b79b1bf5c3af22ba425e629ba590ca617e70c145d9b66d7820996dc1124082435c0643fdfbe602a3176189836edc62a9ad57d4901f7d66b76cc7ac149c108f317ceb33c1d1946fb1d64978fc8ff322b91c0f2ba032a27a84cf1eede8a50e52f22c3a91c472a2e90c13e7fc0623fe9458bba11c6ef34d17ee095ea5ecf5d4e4043bd9ba682129fef79ced2799dcc89fa23a89f90f4ce7ceba073d96c38eb801b75b94f4f91ee47026bca802e1e70ad4ff22b965622da8a1aaa85666e6167ef35ec5fd0d9f925632c6818001eb8d2c9eb5012c590ce2efdf677e5ab223f317d6eac9a3e8d23f93309e88f4d",16)

c = 12225682126551187619399843891561465899608952498495120851070778192443023261485900560363269700242510941697365921981918056191408738905974825435324679841994232057252389709580959723999122054844144379187848417389566267322902673441312265008128249280701778727420570269893119286011513549800540500264752909082405313097299590601819529975638766522951170517766409850156769569563924473524368177233982270360715976884639307240445794551655637991803019693125040126171348043927410721121473304998359286936518573367417946711868112216965614586268606230443139176878435753744068734717043992817907788262531021387616180516736397859628481024223

plain = str(hex(pow(c, d, n)))[2::]
print(''.join([chr(int(''.join(c), 16)) for c in zip(plain[0::2],plain[1::2])]))
```
    
    
