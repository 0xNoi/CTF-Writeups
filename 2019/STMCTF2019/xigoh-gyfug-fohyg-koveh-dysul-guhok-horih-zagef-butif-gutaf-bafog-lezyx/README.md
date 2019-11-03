# xigoh-gyfug-fohyg-koveh-dysul-guhok-horih-zagef-butif-gutaf-bafog-lezyx [CRYPTO]

Sorunun İsmini hatırlamıyorum.

Cryptodan daha çok osint sorusu gibi bişey aslında. ne olduğunu bulursan çözersin temalı. Her neyse, 

Böyle tanımlayamadığım cipherlar ile karşılaştığım da uyguladığım ilk klasik yöntem

Böl > Parçala > Yönet Modeli

Arama motorlarını teker teker dolaşıp ilk iki ifadeyi, parça parça aratmaya başladım hemen

`xigoh gyfug` 

Karşıma çıkan ilk şey bu oldu

![](https://raw.githubusercontent.com/ozancetin/CTF-Writeups/master/2019/STMCTF2019/xigoh-gyfug-fohyg-koveh-dysul-guhok-horih-zagef-butif-gutaf-bafog-lezyx/ScreenShots/1.png)

http://timestamps.keeex.com/3J9nhPaVJtYmgBTCZRatWUSLiuZZo1ih9oRStGM.html

online aşamasındaki osint sorusu aklıma geldi, belki keeex.com'un testserver vardır gibisinden aratmaya başladım 

`keeex test server`	

aratmasında burayı buldum 

![](https://raw.githubusercontent.com/ozancetin/CTF-Writeups/master/2019/STMCTF2019/xigoh-gyfug-fohyg-koveh-dysul-guhok-horih-zagef-butif-gutaf-bafog-lezyx/ScreenShots/2.png)

https://keeex.me/live-demos/

![](https://raw.githubusercontent.com/ozancetin/CTF-Writeups/master/2019/STMCTF2019/xigoh-gyfug-fohyg-koveh-dysul-guhok-horih-zagef-butif-gutaf-bafog-lezyx/ScreenShots/3.png)
![](https://raw.githubusercontent.com/ozancetin/CTF-Writeups/master/2019/STMCTF2019/xigoh-gyfug-fohyg-koveh-dysul-guhok-horih-zagef-butif-gutaf-bafog-lezyx/ScreenShots/4.png)
![](https://raw.githubusercontent.com/ozancetin/CTF-Writeups/master/2019/STMCTF2019/xigoh-gyfug-fohyg-koveh-dysul-guhok-horih-zagef-butif-gutaf-bafog-lezyx/ScreenShots/5.png)

Siteyi biraz kurcaladığımda ne olduğunu buldum

`Bubble Babble Encoding` aradığımız şeydi

Hızlıca decode edebilmek için bir python reposu indirip flagi buldum.

https://github.com/eur0pa/bubblepy

![](![](https://raw.githubusercontent.com/ozancetin/CTF-Writeups/master/2019/STMCTF2019/xigoh-gyfug-fohyg-koveh-dysul-guhok-horih-zagef-butif-gutaf-bafog-lezyx/ScreenShots/Decoded.png))


Flag: `STMCTF{R0tTen_P0t4t0NG}`
