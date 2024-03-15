## **Description**
In "The Ransomware Dystopia," LockTalk emerges as a beacon of resistance against the rampant chaos inflicted by ransomware groups. In a world plunged into turmoil by malicious cyber threats, LockTalk stands as a formidable force, dedicated to protecting society from the insidious grip of ransomware. Chosen participants, tasked with representing their districts, navigate a perilous landscape fraught with ethical quandaries and treacherous challenges orchestrated by LockTalk. Their journey intertwines with the organization's mission to neutralize ransomware threats and restore order to a fractured world. As players confront internal struggles and external adversaries, their decisions shape the fate of not only themselves but also their fellow citizens, driving them to unravel the mysteries surrounding LockTalk and choose between succumbing to despair or standing resilient against the encroaching darkness.
<br></br>
In `config.py` we can see that the token was generated using RSA so we can't bruteforce the token

```py
JWT_SECRET_KEY = jwk.JWK.generate(kty='RSA', size=2048)
```
In requirements.txt we can see that it's using an old version of JWT `python_jwt==3.3.3`, Which is vulnerable :L according to this : `https://github.com/advisories/GHSA-5p8v-58qm-c7fp`
<img src="https://github.com/Yazan03/CTF-Writeups2024/blob/main/HTB_cyber_apocalypse/WEB/images/4.PNG">

