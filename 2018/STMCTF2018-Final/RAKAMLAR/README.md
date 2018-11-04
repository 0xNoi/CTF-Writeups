# Rakamlar
Bu soruda bize:
```
147896532 14789653 14789635 74269 14789632
```
5 tane anlamsız diyebileceğimiz sayı verilmişti ve bu sayıların plaintext halini bulmamızı istemişti.

flag formatı STMCTF{} bizim eklememiz gerekiyordu.

Açık söylemek gerekirse bu soruyu en hızlı OSINT yaparak ve tahmin ederek buldum.

Googlea girip "147896532 crypto" diye bi arama yaptığımda karşıma çıkan ilk sayfaya girdim. Bu sayfa bir reddit içeriğiydi. 
Daha önce buna benzer bir ciphertext verilmiş ve birisi o ciphertexti substitution yaparak çözmüş.

![](https://raw.githubusercontent.com/ozancetin/CTF-Writeups/master/2018/STMCTF2018-Final/RAKAMLAR/1.png)
![](https://raw.githubusercontent.com/ozancetin/CTF-Writeups/master/2018/STMCTF2018-Final/RAKAMLAR/2.png)

kaynak: https://www.reddit.com/r/codes/comments/9k3i4e/a_short_story_encrypted_with_many_different/

ciphertextteki sayılar ile plaintextteki harfleri buldum eşleştirdim

147896532 = b 
14789653  = r
14789635  = a
74269 	  = ?
14789632  = o


74269 sayısının ne olduğunu sayfada bulamadım ama çok kısacık bi düşünmeyle ile cevabın "bravo" olabileceğini tahmin ettim ve ilk denemede flagi buldum. 
```
Dolayısıyla flag: STMCTF{bravo}
```




