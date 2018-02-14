# SEVGİLİ GÜNLÜK (CRYPTO 100)
```
Challenge : Mahmut Pelinsu'nun gizli mesajlarını içeren günlüğünü elde etmişti. İlk sayfalarda Pelinsu'nun amatörce kullandığı şifreleme algoritmaları hemen dikkatini çekti. İşe koyulmuştu. 
```
[SevgiliGünlük.zip](https://github.com/ozancetin/CTF-Writeups/blob/master/2018/DKHOSCTF/Sevgili%20G%C3%BCnl%C3%BCk/SevgiliG%C3%BCnl%C3%BCk.zip?raw=true)

Verilen sıkıştırılmış dosyanın içerisinde [flag.txt.enc](https://raw.githubusercontent.com/ozancetin/CTF-Writeups/master/2018/DKHOSCTF/Sevgili%20G%C3%BCnl%C3%BCk/flag.txt.enc) ve [public.key](https://raw.githubusercontent.com/ozancetin/CTF-Writeups/master/2018/DKHOSCTF/Sevgili%20G%C3%BCnl%C3%BCk/public.key) mevcut.

Public Keyimiz
```
-----BEGIN PUBLIC KEY-----
MHQwDQYJKoZIhvcNAQEBBQADYwAwYAJZAMm8boGdMWojp16imqdChjRhfAmm53ol
yIhM1AXft8qjcF2P1cfb0ZMOrbP7TUYB4zCt0SH098xRUlOxAdMQ2duzpy7KNqHe
Yqb01XP1+3HK2wF1edzhSekCAwEAAQ==
-----END PUBLIC KEY-----
```
Encrypted Flag
```
~}�<��6
2m^j'��j��%���/�Y[ڵ����:K�Q�0�e�q�-�c|GzM.���G��)�e���R�B�b��f9q�J
```

Kısaca açıklamak gerekirse,
Public Key sadece Modu(N) ve Exponenti(e) içerir. 
N sayısı, p ve q olan 2 tane asal sayı ile kolayca faktorize edilebilir bi sayı olarak verilmiş. Bu durumda N = p x q.
Böylece p ve q sayısını kullanarak private key üretebiliriz ve bize verilen encrypted veriyi decrypt edebiliriz.


Openssl yardımıyla 704 bitlik RSA Public Key olduğunu öğreniyoruz. Faktorizasyon işlemini kolaylaştırmak için hexadecimalden decimal sayıya çevirdik.

![](https://raw.githubusercontent.com/ozancetin/CTF-Writeups/master/2018/DKHOSCTF/Sevgili%20G%C3%BCnl%C3%BCk/1.png)

```
openssl rsa -noout -text -inform PEM -in public.key -pubin
```
```python
python -c "print(int('00c9bc6e819d316a23a75ea29aa7428634617c09a6e77a25c8884cd405dfb7caa3705d8fd5c7dbd1930eadb3fb4d4601e330add121f4f7cc515253b101d310d9dbb3a72eca36a1de62a6f4d573f5fb71cadb017579dce149e9', 16))"
```
Faktorizasyon işlemi için bi bruteforce kodu yazabilirsiniz fakat kullandığınız bilgisayarınıza göre süresi çok uzun sürebilir. Online olarak kullanabileceğiniz geniş database sahip http://www.factordb.com/index.php web sitesinden yararlanabilirsiniz.

![](https://raw.githubusercontent.com/ozancetin/CTF-Writeups/master/2018/DKHOSCTF/Sevgili%20G%C3%BCnl%C3%BCk/2.png)

Sayıyı faktorize edebildik 
```
(8143859259110045265727809126284429335877899002167627883200914172429324360133004116702003240828777970252499)^2
```
106 basamaklı asal sayının karesi olarak çıktığı için bu durumda p ve q asal değerlerimiz birbirine eşit 

Private key üretmek için RSATOOL genelde sıkça kullanılan bi python scripti

![](https://raw.githubusercontent.com/ozancetin/CTF-Writeups/master/2018/DKHOSCTF/Sevgili%20G%C3%BCnl%C3%BCk/3.png)

```
rsatool -p 8143859259110045265727809126284429335877899002167627883200914172429324360133004116702003240828777970252499 -q 8143859259110045265727809126284429335877899002167627883200914172429324360133004116702003240828777970252499 -o private.key
```
Ürettiğimiz Private Key
```
-----BEGIN RSA PRIVATE KEY-----
MIIBewIBAAJZAMm8boGdMWojp16imqdChjRhfAmm53olyIhM1AXft8qjcF2P1cfb0ZMOrbP7TUYB
4zCt0SH098xRUlOxAdMQ2duzpy7KNqHeYqb01XP1+3HK2wF1edzhSekCAwEAAQJZAMjjue+ch464
fn0A05zn5BjZUtmRuUSrx2vjhedrhuxloQmqqCpjvekBXvywy06vwgWHiys/KhQ0Qbw9fmHtJDU5
46BOoUT+tHEmhJWCFpdDLOZQ5JrF2nUCLQDjQQ2E7oFs6+jJb1N0q/Q/K03E7O3+xlgq/cjKGdLR
T4BJX9ni7nNWp4e60wItAONBDYTugWzr6MlvU3Sr9D8rTcTs7f7GWCr9yMoZ0tFPgElf2eLuc1an
h7rTAiwn2IkpTLRux7JqV1W3uEq8JLifFbfpGxfsedER9pMrVhg1RVQr4QliIT/ANwIsJ9iJKUy0
bseyaldVt7hKvCS4nxW36RsX7HnREfaTK1YYNUVUK+EJYiE/wDcCAQA=
-----END RSA PRIVATE KEY-----
```
Private Keyi ürettiğimize göre encrypted veriyi yine openssl yardımıyla decrypt edebiliriz
![](https://raw.githubusercontent.com/ozancetin/CTF-Writeups/master/2018/DKHOSCTF/Sevgili%20G%C3%BCnl%C3%BCk/4.png)

```
openssl rsautl -decrypt -in flag.txt.enc -out flag.txt -inkey private.key
```
Sonuç olarak elde ettiğimiz flag:

```
DKHOS_{b4by_h3ll0_w0rld_crypt0_b4by}
```


Son olarak üzücü olan şey şu ki bu soruyu, faktorize işlemini yaptıktan sonra elde edilen asal sayıyı defalarca yanlış kopyaladığım için sorudan pes edip yarışma devam ederken flagi decrypt edemedim. Yarışma sonrasında çözüp buraya unutmamak adına bu write upı paylaşıyorum! :D


