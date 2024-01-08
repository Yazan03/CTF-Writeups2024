# Write up for all OSINT challenges in Iris CTF 2024.
***First challenge :***


<img src="https://github.com/Yazan03/CTF-Writeups2024/blob/main/OSINT/IrisCTF/assets/1.png">

The download file has this picture.

<img src="https://github.com/Yazan03/CTF-Writeups2024/blob/main/OSINT/IrisCTF/assets/2.png">

When you search for a Google image about it, you will find a similar image in a blog post.  

<img src="https://github.com/Yazan03/CTF-Writeups2024/blob/main/OSINT/IrisCTF/assets/3%20(2).png">

Inside it, there is a place called "Prague Castle."

<img src="https://github.com/Yazan03/CTF-Writeups2024/blob/main/OSINT/IrisCTF/assets/4.png">

After searching around, there is a street close to it called "Zlatá ulička u Daliborky."

<img src="https://github.com/Yazan03/CTF-Writeups2024/blob/main/OSINT/IrisCTF/assets/5.png">

After browsing street view images, I found the place.

<img src="https://github.com/Yazan03/CTF-Writeups2024/blob/main/OSINT/IrisCTF/assets/6.png">

The flag : ***irisctf{zlata_ulicka_u_daliborky}***






===================================================================================================================================


***Second challenge :***

<img src="https://github.com/Yazan03/CTF-Writeups2024/blob/main/OSINT/IrisCTF/assets/7.png">

Using ```https://epieos.com/``` to search for the email address, I found the username.

<img src="https://github.com/Yazan03/CTF-Writeups2024/blob/main/OSINT/IrisCTF/assets/8.png">

I got his account in Instagram: 

<img src="https://github.com/Yazan03/CTF-Writeups2024/blob/main/OSINT/IrisCTF/assets/9.png">
One of the posts has the flag:


<img src="https://github.com/Yazan03/CTF-Writeups2024/blob/main/OSINT/IrisCTF/assets/10.png">





========================================================================================================================

***Third challenge :***

<img src="https://github.com/Yazan03/CTF-Writeups2024/blob/main/OSINT/IrisCTF/assets/11.png">
We are given a link to a webpage; let's jump into it.

<img src="https://github.com/Yazan03/CTF-Writeups2024/blob/main/OSINT/IrisCTF/assets/12.png">
The username is ```iris stein``` and it has a LinkedIn account: 

<img src="https://github.com/Yazan03/CTF-Writeups2024/blob/main/OSINT/IrisCTF/assets/13.png">
For the third question : ```Mountain Peak Hiring Agency```

Then from the ```michelangelo corning``` Instagram: From his following, we get Iris's IG: 

<img src="https://github.com/Yazan03/CTF-Writeups2024/blob/main/OSINT/IrisCTF/assets/14.png">
In one of her posts, she mentioned her mom.

<img src="https://github.com/Yazan03/CTF-Writeups2024/blob/main/OSINT/IrisCTF/assets/15.png">
Then I found her mom's Facebook account.

<img src="https://github.com/Yazan03/CTF-Writeups2024/blob/main/OSINT/IrisCTF/assets/16.png">
Also, she is mentioned at some live events, one of which is her third birthday date.

<img src="https://github.com/Yazan03/CTF-Writeups2024/blob/main/OSINT/IrisCTF/assets/17.png">
So we got her age: ```27```, and we still want the hospital where Iris was born. If we clicked on Iris's birthday, she put a picture from the hospital. 

<img src="https://github.com/Yazan03/CTF-Writeups2024/blob/main/OSINT/IrisCTF/assets/18.png">
Using Google Image, we will get the hospital name: ```Lenox Hill Hospital```

<img src="https://github.com/Yazan03/CTF-Writeups2024/blob/main/OSINT/IrisCTF/assets/19.png">
Combined everything together to get the flag. 

<img src="https://github.com/Yazan03/CTF-Writeups2024/blob/main/OSINT/IrisCTF/assets/20.png">





=============================================================================================================================

***Last challenge :***

With First blood !

<img src="https://github.com/Yazan03/CTF-Writeups2024/blob/main/OSINT/IrisCTF/assets/21.png">
We are given a hash, and the flag is the cleartext of the password. The goal is to make a specific list for ```irirs```, Let's get back to her IG. We will notice some pisces we can get to help us:

<img src="https://github.com/Yazan03/CTF-Writeups2024/blob/main/OSINT/IrisCTF/assets/22.png">
<img src="https://github.com/Yazan03/CTF-Writeups2024/blob/main/OSINT/IrisCTF/assets/23.png">
<img src="https://github.com/Yazan03/CTF-Writeups2024/blob/main/OSINT/IrisCTF/assets/24.png">

Her mom's date is from her Facebook: 

<img src="https://github.com/Yazan03/CTF-Writeups2024/blob/main/OSINT/IrisCTF/assets/26.png">
Then I made a script to generate all the combinations from her account and added more.

```py
from itertools import permutations

words = ["Iris", "Stein", "Elaine", "Tiramisu", "Portofino", "Mimosas", "Italy"]
word_combinations = permutations(words, 3)
all_word_combinations = [''.join(combo) for combo in word_combinations]

date_numbers = "8041965"
num_combinations = permutations(date_numbers, len(date_numbers))
all_num_combinations = [''.join(combo) for combo in num_combinations]

combined_results = [word_combo + num_combo for word_combo in all_word_combinations for num_combo in all_num_combinations]

for i in combined_results :
    print(i)
```

```john hash --wordlist=out.txt```

The password will be : ```PortofinoItalyTiramisu0481965```

The Final flag : ***irisctf{PortofinoItalyTiramisu0481965}***
