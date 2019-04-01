# Sunshine CTF 2019 ALL CRYPTO CHALLENGES WRITEUPS
# Welcome Crypto [50]

```
~C8 =39 A?2V8 73J:C 8FG7 AF?JJC2ECP

DF?LHb=r_>b0%_0520<c8bPN
```

Its ROT 47

```
Org lbh pna'g fbyir guvf punyyratr!

sun{w3lC0m3_T0_da_k4g3!}
```

# CB1 [50]

Given in CB1.wav

Its Amateur Radio Phonetic Alphabet

When we listen and convert cipher is :

```
hkcgxkznkojkyulsgxin
```
And try Caesar Cipher

Here's flag: ```BEWARETHEIDESOFMARCH```
its maybe lower case I dont remember exactly.

# CB2 [100]

Given in CB2.wav

Its same thing again Phonetic Alphabet

But this time be careful in begining part he said :
```
Codeword : clarinet

And Cipher is : DBDAABEDDDDCDEACADBBDDADDEABBB
```
And as you can see cipher became only "A B C D E" 

First idea come up Polybius Cipher, I divide and convert number version: 

```
DB DA AB ED DD DC DE AC AD BB DD AD DE AB BB

42 41 12 54 44 43 45 13 14 22 44 14 45 12 22
```

and new cipher here is.

When you try Decode

```
Cipher : 42 41 12 54 44 43 45 13 14 22 44 14 45 12 22
Key: clarinet
```
You can use your code, by hand or quickly try online tool:

https://md5decrypt.net/en/Polybius-square/

flag is : ```polysquaresrule ```

# CB3 [150]

Given in CB3.wav

Its same thing again Phonetic Alphabet


Begining part he said:
```
Codeword: prideful
Cipher  : XDXGFVVVXXAFVFFVADGDDXAGAAFDFFFF
```

Idk cipher what this is, but I just a bit google search like a identify cipher unique letters and order alphabetically

ADFGVX cipher

And when u quickly try to decode

https://www.dcode.fr/adfgvx-cipher

```
Cipher  : XDXGFVVVXXAFVFFVADGDDXAGAAFDFFFF
Key     : prideful 
```

Flag is ```g3rm4n3ncrypt10n``` 

# ArbEncrypt [200]

This challenge made me crazy 

They gave hint ```France0110 has a meaning, it relates to what was used to encode the message.```

France Part is obviously = Vigenere Cipher

0110 = is obviously Xor operation Truth Table

but we got a base64 ciphertext, its must be xor part but there is no key.

Here's cipher

```
BBcEDAJCDBMIAxUHA3gQBxEXCwdCAwQPDhxCGRMNawYHBRgDDQcNBRAWGxZCABoUAHgQBREEDwIQDgtCCx8DFR4RaxwLGFIWERQVBxdCGQgPBBARChgBaxYSFRQRAgIGDQRCFxwYAgAEGXgHDhgRChQMChgDAlITDQAWFQgGQRcNFAAQQR0LGRsWAghCAhQaa3gGExwMQRMEFRkIEhQNQRUEERYRGxdCChsQBwQFGHgEFwQRGBkLCBcKQREUDgYUElIVGAJoEhUIBQQRGFIWERwWFxAYDhdoBhAOF1IPCAYOCBkYTAEFDBsJQQEHBQIQCxRoFwgXABYID1IQBgYUElIEBwEBF3gADRsEAAcYQRwUFQYUBFIKDRwDBFIaCBcEa1IRDR0ZABsBPgsEFy0KEwMSES0XDi0IBxc9BRQ9UEJSUENRUUdTWA8=
```

After read many times challenge description I recognized this part

```It's pretty ARB-itrary. France0110.```

I thought "ARB" may be key but its no luck a bit corrupted results.

After hours I try lower case xor key as "arb". Thanks to lowercase. It worked.

Here's cipher hex values 

```
417040c02420c13080315070378100711170b074203040f0e1c4219130d6b06070518030d070d0510161b1642001a140078100511040f02100e0b420b1f03151e116b1c0b18521611141507174219080f0410110a18016b16121514110202060d0442171c180200041978070e18110a140c0a18030252130d001615080641170d140010411d0b191b1602084202141a6b7806131c0c41130415190812140d4115041116111b17420a1b1007040518780417041118190b08170a4111140e0614125215180268121508050411185216111c161710180e176806100e17520f08060e0819184c01050c1b094101070502100b14681708170016080f52100606141252040701011778000d1b04000718411c1415061404520a0d1c0304521a0817046b52110d1d19001b013e0b04172d0a130312112d170e2d0807173d05143d504252504351514753580f
```

XOR

```
6172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172626172
```
(arb) iterate same length with cipher but be careful last part you need to delete 1 byte like a  ```...arbarbar[deleted]```

```
eefmp majbgeb
rfcuju bvmon xao
tedjaluodbtzd ahva
rdcfnproy jmatls
niy tpfwfe xzmebskjc
dptfscpdlv vnzcrfx
eojskfnkjac qlrttzd eourr oixitcz cfx

drnn aftkjsfo gfpdsze kirfvgy
fvvsykiieh cvotvs wyp
sgjdvsy tpntvbzoe
gblv mitlikz-sgmik sedprjf
vzuadjn rgtvs ffscv
blifauz nvttve hlnae xief
 slo{aic_yfv_hrqpp_uo_jfe_df_1001130519}
 ```

And now we can try vigenere with same key

key: arb

```
enemy lasagna
robust below wax
semiautomatic aqua
accompany slacks
why coffee gymnastic
motorcycle unibrow
existential plastic extra nightly cow

damn jettison goodbye through
everything center who
spidery concubine
pale lickity-split remorse
vitamin after force
already nested human wine
 sun{arb_you_happy_to_see_me_1001130519}
 ```

# 16-BIT-AES [100]

This answer describe as well why is not 16 bit aes exist.
https://crypto.stackexchange.com/questions/35117/are-there-attacks-on-aes-with-16-bit-keys

So if they use AES-128-ECB and key is 16 bit, key must be iterate itself so which means that we can find that key quickly bruteforce.

And I recognized everyconnection use same key that much easy. I create basic input and took encoded version then bruteforce this script.

```python

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
#decipher = AES.new("fL"*8, AES.MODE_ECB)
#m=decipher.encrypt("BnMb7wu7tD3wYAYv")
#print(m.encode("hex"))
```

And key is became ```fL```

Then we can find quickly flag.

Encrypt given text with that key

```fLfLfLfLfLfLfLfL```

and get flag


Flag is : 
```Correct! The flag is sun{Who_kn3w_A3$_cou1d_be_s0_vulner8ble?}```