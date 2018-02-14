# SEVGİLİ GÜNLÜK (CRYPTO 100)

Challenge : Mahmut Pelinsu'nun gizli mesajlarını içeren günlüğünü elde etmişti. İlk sayfalarda Pelinsu'nun amatörce kullandığı şifreleme algoritmaları hemen dikkatini çekti. İşe koyulmuştu. 

[SevgiliGünlük.zip](https://github.com/ozancetin/CTF-Writeups/blob/master/2018/DKHOSCTF/Sevgili%20G%C3%BCnl%C3%BCk/SevgiliG%C3%BCnl%C3%BCk.zip?raw=true)

Verilen sıkıştırılmış dosyanın içerisinde [flag.txt.enc](https://raw.githubusercontent.com/ozancetin/CTF-Writeups/master/2018/DKHOSCTF/Sevgili%20G%C3%BCnl%C3%BCk/flag.txt.enc) ve [public.key](https://raw.githubusercontent.com/ozancetin/CTF-Writeups/master/2018/DKHOSCTF/Sevgili%20G%C3%BCnl%C3%BCk/public.key) mevcut.

Kısaca açıklamak gerekirse,
Public Key sadece Modu(N) ve Exponenti(e) içerir. 
N sayısı, p ve q 2 tane asal sayı ile kolayca faktörize edilebilir bi sayı olarak verilmiş. Bu durumda N = p x q
Böylece p ve q sayısını kullanarak private key üretebiliriz ve bize verilen encrypted veriyi decrypt edebiliriz.

1. Openssl yardımıyla 704 bitlik RSA Public Key olduğunu öğreniyoruz. Faktörizasyon işlemini kolaylaştırmak için hexten decimal sayıya çevirdik.

![](https://raw.githubusercontent.com/ozancetin/CTF-Writeups/master/2018/DKHOSCTF/Sevgili%20G%C3%BCnl%C3%BCk/1.png)

```
openssl rsa -noout -text -inform PEM -in public.key -pubin
```
```python
python -c "print(int('00c9bc6e819d316a23a75ea29aa7428634617c09a6e77a25c8884cd405dfb7caa3705d8fd5c7dbd1930eadb3fb4d4601e330add121f4f7cc515253b101d310d9dbb3a72eca36a1de62a6f4d573f5fb71cadb017579dce149e9', 16))"
```


