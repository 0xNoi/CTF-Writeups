# How much can you throw on a Caesar salad?

```
Challenge: Cryptography is the art of hiding things. there are multiple ways to do it. There are multiple layers to this message. When you find the answer then make it a flag.. mihi nomen latine! Example: flag{WORDS_WORDS_WORDS}
```
Here's the given jpeg file
![](https://raw.githubusercontent.com/ozancetin/CTF-Writeups/master/2018/NeverLAN%20CTF%202018/How%20much%20can%20you%20throw%20on%20a%20Caesar%20salad%3F/O_SO_Curious.jpeg)

Looks like stego challenge in there

Then I tried steghide 
Password should be "neverlan" but it didnt work then tried "neverlanctf" so it worked and extracted WhyS0CuR1o5.txt
![](https://raw.githubusercontent.com/ozancetin/CTF-Writeups/master/2018/NeverLAN%20CTF%202018/How%20much%20can%20you%20throw%20on%20a%20Caesar%20salad%3F/1.png)

in WhyS0CuR1o5.txt looks like base64, I decoded output is some binary values again I tried binary to ascii, heres the some ciphertext and I tried caeser bruteforced it worked.
```
MDEwMDExMDAgMDExMDAxMDEgMDExMTAxMTEgMDExMDExMDAgMDExMTEwMDEgMDExMTAwMDAgMDExMDExMDAgMDExMTAxMDEgMDExMDEwMTAgMDExMDExMDAgMDAxMDAwMDAgMDExMTAwMDAgMDExMTEwMTAgMDAxMDAwMDAgMDExMDAwMDEgMDExMDExMTEgMDExMDExMDAgMDAxMDAwMDAgMDEwMDAwMDEgMDExMDExMDAgMDExMDEwMDAgMDExMDEwMTAgMDExMDExMTEgMDExMDExMDAgMDExMTEwMDEgMDAxMDAwMDAgMDExMTAxMTAgMDExMDExMDEgMDAxMDAwMDAgMDExMDEwMDAgMDExMTAwMTEgMDExMTAwMTEgMDAxMDAwMDAgMDExMDAwMDEgMDExMDExMTEgMDExMTAwMDAgMDExMTAxMDEgMDExMDExMTAgMDExMTEwMTAgMDAwMTAxMA==
```

![](https://raw.githubusercontent.com/ozancetin/CTF-Writeups/master/2018/NeverLAN%20CTF%202018/How%20much%20can%20you%20throw%20on%20a%20Caesar%20salad%3F/2.png)
```
01001100 01100101 01110111 01101100 01111001 01110000 01101100 01110101 01101010 01101100 00100000 01110000 01111010 00100000 01100001 01101111 01101100 00100000 01000001 01101100 01101000 01101010 01101111 01101100 01111001 00100000 01110110 01101101 00100000 01101000 01110011 01110011 00100000 01100001 01101111 01110000 01110101 01101110 01111010 0001010
```
![](https://raw.githubusercontent.com/ozancetin/CTF-Writeups/master/2018/NeverLAN%20CTF%202018/How%20much%20can%20you%20throw%20on%20a%20Caesar%20salad%3F/3.png)
```
Lewlyplujl pz aol Alhjoly vm hss aopunz
```

![](https://raw.githubusercontent.com/ozancetin/CTF-Writeups/master/2018/NeverLAN%20CTF%202018/How%20much%20can%20you%20throw%20on%20a%20Caesar%20salad%3F/4.png)
```
EXPERIENCE IS THE TEACHER OF ALL THINGS
```
I searched this words in google and its Caesar Words
![](https://raw.githubusercontent.com/ozancetin/CTF-Writeups/master/2018/NeverLAN%20CTF%202018/How%20much%20can%20you%20throw%20on%20a%20Caesar%20salad%3F/5.png)

Original full name Gaius Julius Caesar
![](https://raw.githubusercontent.com/ozancetin/CTF-Writeups/master/2018/NeverLAN%20CTF%202018/How%20much%20can%20you%20throw%20on%20a%20Caesar%20salad%3F/6.png)

When I found this, tried almost all combinations
like
```
flag{Gaius_Juluis_Caesar}
flag{Juluis_Caesar_Gaius}
flag{Caesar_Gaius_Julius}
```
But these didnt work

After then research in google about Caesar I found his latin name
![](https://raw.githubusercontent.com/ozancetin/CTF-Writeups/master/2018/NeverLAN%20CTF%202018/How%20much%20can%20you%20throw%20on%20a%20Caesar%20salad%3F/7.png)

CAIVS IVLIVS CAESAR
so flag must be:

```
flag{CAIVS_IVLIVS_CAESAR}
```





