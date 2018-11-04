# Tuzlama

Yarışma esnasında screenshot alamadım ama aklımda kalanlar ile çözümünü anlatıyorum.

Tuzlama sorusunda bize bir zip dosyası ile bir web sitesi veriliyor. Zip dosyasının içerisinde parolalı bir flag.rar dosyası ve encrypted.pass adlı şifrelenmiş bir data mevcut.
![](https://raw.githubusercontent.com/ozancetin/CTF-Writeups/master/2018/STMCTF2018-Final/Tuzlama/tuzlama.zip)
![](https://raw.githubusercontent.com/ozancetin/CTF-Writeups/master/2018/STMCTF2018-Final/Tuzlama/1.png)

Web sitesi ise sadece 2 tane .pdf dosyası upload edebilecek şekilde tasarlanmış. Bizden öyle 2 pdf dosyası istiyor ki pdflerin SHA1 özetleri aynı, MD5 özetleri farklı olmalı.

İnternette biraz araştırmamız sonucunda github da

https://github.com/nneonneo/sha1collider

Şu repoya ulaştık.

![](https://raw.githubusercontent.com/ozancetin/CTF-Writeups/master/2018/STMCTF2018-Final/Tuzlama/2.png)

Hatta repo içerisinde örnek olarak verdiği pdf dosyaları tam istediğimiz gibi SHA1 özetleri aynı, MD5 özetleri farklı.

![](https://raw.githubusercontent.com/ozancetin/CTF-Writeups/master/2018/STMCTF2018-Final/Tuzlama/3.png)
![](https://raw.githubusercontent.com/ozancetin/CTF-Writeups/master/2018/STMCTF2018-Final/Tuzlama/4.png)

Bize verilen websitesine, bulduğumuz ya da ürettiğimiz istenilen 2 pdf dosyasını da yüklediğimizde döndürdüğü başarılı sorgu:

```
Algorithm: AES-256-CBC
Key: 1sTm_2Ctf_3cRyPto!
```
Openssl kullanarak encrypted datayı decrypt edebildim. Ve bir Nusret jpeg dosyası çıktı.

![](https://raw.githubusercontent.com/ozancetin/CTF-Writeups/master/2018/STMCTF2018-Final/Tuzlama/5.png)
![](https://raw.githubusercontent.com/ozancetin/CTF-Writeups/master/2018/STMCTF2018-Final/Tuzlama/5.png)
![](https://raw.githubusercontent.com/ozancetin/CTF-Writeups/master/2018/STMCTF2018-Final/Tuzlama/pass_decrypted.jpeg)

Bu noktadan sonra çok takıldım. Çünkü fotoğrafta hiçbir mantıklı bişey yoktu. Stego olabileceğini düşündüm kurcaladım ama yine bişey çıkmadı. Daha sonra soruya bir hint geldi tam olarak hint cümlesini hatırlamıyorum ama verdiği şey "Nusretten çıkıp tuzlamayı dışarıda aramamız gerektiği" ile ilgiliydi. Bi çeşit nusret fotoğrafı yanıltmaca olarak koyulmuştu.

Opensslde salt ile ilgili araştırma yaptıktan sonra decrypt edilirken "-p" parametresi kullanılırsa salt değeri, keyi ve init vektörü ekrana bastırdığını öğrendim. Denediğimde salt değerinin hex versiyonu çıktı.
Bu değeri flag.rar için parola olarak denediğimde işe yaradı. 

![](https://raw.githubusercontent.com/ozancetin/CTF-Writeups/master/2018/STMCTF2018-Final/Tuzlama/6.png)
![](https://raw.githubusercontent.com/ozancetin/CTF-Writeups/master/2018/STMCTF2018-Final/Tuzlama/7.png)
![](https://raw.githubusercontent.com/ozancetin/CTF-Writeups/master/2018/STMCTF2018-Final/Tuzlama/8.png)

```
Flag: STMCTF{hashden_g1rd1k_tuzdan_c1kt1k}
```
Öte yandan bu soruya en süslüsünden bi parantez açmak istiyorum.

Eğer en başta pass.encrypted datasının içerisindeki 

![](https://raw.githubusercontent.com/ozancetin/CTF-Writeups/master/2018/STMCTF2018-Final/Tuzlama/9.png)

"Salted__hagayret" üzerine yoğunlaşıp, ASCII To Hex yapmış olsaydık, soruya dair hiçbir şeyle uğraşmadan rarın parolasına direk ulaşabilirdik ve tabii ki flage de...

hagayret = 6861676179726574



