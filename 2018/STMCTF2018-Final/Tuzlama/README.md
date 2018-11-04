#Tuzlama

Tuzlama sorusunda bize bir zip dosyası ile bir web sitesi veriliyor. Zip dosyasının içerisinde parolalı bir flag.rar dosyası ve encrypted.pass adlı şifrelenmiş bir data mevcut. Web sitesi ise sadece 2 tane .pdf dosyası upload edebilecek şekilde tasarlanmış. Bizden öyle 2 pdf dosyası istiyor ki pdflerin SHA1 özetleri aynı, MD5 özetleri farklı olmalı.

İnternette biraz araştırmamız sonucunda github da

https://github.com/nneonneo/sha1collider

Şu repoya ulaştık.

Hatta repo içerisinde örnek olarak verdiği pdf dosyaları tam istediğimiz gibi SHA1 özetleri aynı, MD5 özetleri farklı.

Bize verilen websitesine, bulduğumuz ya da ürettiğimiz istenilen 2 pdf dosyasını da yüklediğimizde döndürdüğü başarılı sorgu:

Algorithm: AES-256-CBC
Key: 1sTm_2Ctf_3cRyPto!


Openssl kullanarak encrypted datayı decrypt edebildim. Ve bir Nusret jpeg dosyası çıktı.

Bu noktadan sonra çok takıldım. Çünkü fotoğrafta hiçbir mantıklı bişey yoktu. Stego olabileceğini düşündüm kurcaladım ama yine bişey çıkmadı. Daha sonra soruya bir hint geldi tam olarak hint cümlesini hatırlamıyorum ama verdiği şey "Nusretten çıkıp tuzlamayı dışarıda aramamız gerektiği" ile ilgiliydi. Bi çeşit nusret fotoğrafı yanıltmaca olarak koyulmuştu.

Opensslde salt ile ilgili araştırma yaptıktan sonra decrypt edilirken "-p" parametresi kullanılırsa salt değeri, keyi ve init vektörü ekrana bastırdığını öğrendim. Denediğimde salt değerinin hex versiyonu çıktı.
Bu değeri flag.rar için parola olarak denediğimde işe yaradı. 

flag: STMCTF{hashden_g1rd1k_tuzdan_c1kt1k}

Öte yandan bu soruya en süslüsünden bi parantez açmak istiyorum.

Eğer en başta pass.encrypted datasının içerisindeki 

"Salted__hagayret"

üzerine yoğunlaşıp

hagayret = 6861676179726574

ASCII To Hex yapmış olsaydık, soruya dair hiçbir şeyle uğraşmadan rarın parolasına direk ulaşabilirdik ve tabiiki flage.
