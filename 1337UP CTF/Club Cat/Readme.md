## **Description**
People are always complaining that there's not enough cat pictures on the internet.. Something must be done!!
<br></br>

Reading the source code foud that JWT Rs256 keys are publicly accesable on /jwks.json route.
<img src="https://github.com/Yazan03/CTF-Writeups2024/blob/main/1337UP%20CTF/Club%20Cat/images/Capture.PNG">
<br></br>

So We can make a key confusion attack as descriped here

https://portswigger.net/web-security/jwt/algorithm-confusion

