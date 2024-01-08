# Write up for all OSINT challenges in Iris CTF 2024.
***First challenge :***


![image](https://github.com/Yazan03/Priv/assets/94278827/3593cfd4-76b4-4a8b-9652-a0a1f1255db0)

The download file has this picture.

![image](https://github.com/Yazan03/Priv/assets/94278827/b7a36d3a-e910-4b31-9bcb-adb4d8881db4)

When you search for a Google image about it, you will find a similar image in a blog post.  

![Screenshot 2024-01-06 152744](https://github.com/Yazan03/Priv/assets/94278827/3347e681-95c1-4ccc-b510-85df66a82090)

Inside it, there is a place called "Prague Castle."

![image](https://github.com/Yazan03/Priv/assets/94278827/2528cf22-ffbb-4cf6-95c9-d496e6363b78)

After searching around, there is a street close to it called "Zlatá ulička u Daliborky."

![image](https://github.com/Yazan03/Priv/assets/94278827/2d96a21b-99f2-473a-8520-0468db3961c4)

After browsing street view images, I found the place.

![image](https://github.com/Yazan03/Priv/assets/94278827/8ed7a253-5ca3-4b46-8b05-e8fb3e963625)

The flag : ***irisctf{zlata_ulicka_u_daliborky}***






===================================================================================================================================


***Second challenge :***

![image](https://github.com/Yazan03/Priv/assets/94278827/8fc87b0f-8b86-4949-8125-3a54c245a461)

Using ```https://epieos.com/``` to search for the email address, I found the username.

![image](https://github.com/Yazan03/Priv/assets/94278827/8db127fc-ae3d-4931-8e07-0ecc269b6165)

I got his account in Instagram: 

![image](https://github.com/Yazan03/Priv/assets/94278827/b1c187cd-b52a-4b56-b827-a63abe824256)

One of the posts has the flag:


![image](https://github.com/Yazan03/Priv/assets/94278827/7a3d21a0-a27f-4ad0-8390-94adb065f46e)






========================================================================================================================

***Third challenge :***

![image](https://github.com/Yazan03/Priv/assets/94278827/ccb91e8b-9b98-4abc-80d5-b642ecf3c521)

We are given a link to a webpage; let's jump into it.

![image](https://github.com/Yazan03/Priv/assets/94278827/ae2fe3ad-326b-4755-8731-f144afa93e63)

The username is ```iris stein``` and it has a LinkedIn account: 

![image](https://github.com/Yazan03/Priv/assets/94278827/99572c01-aefb-4a70-88d3-34f5f131820b)

For the third question : ```Mountain Peak Hiring Agency```

Then from the ```michelangelo corning``` Instagram: From his following, we get Iris's IG: 

![image](https://github.com/Yazan03/Priv/assets/94278827/018632c9-aba3-410e-83cb-0890a0ce3cf5)

In one of her posts, she mentioned her mom.

![image](https://github.com/Yazan03/Priv/assets/94278827/676f3e28-cf47-4699-9b15-fabb5f9dee9b)

Then I found her mom's Facebook account.

![image](https://github.com/Yazan03/Priv/assets/94278827/6dc6152f-5fba-4716-9cff-6f5e7d059ff7)

Also, she is mentioned at some live events, one of which is her third birthday date.

![image](https://github.com/Yazan03/Priv/assets/94278827/4c1fa3c7-0983-4574-8889-49047b1e93a2)

So we got her age: ```27```, and we still want the hospital where Iris was born. If we clicked on Iris's birthday, she put a picture from the hospital. 

![image](https://github.com/Yazan03/Priv/assets/94278827/dae74cbd-698b-4ff1-b1f8-a4863f23a539)

Using Google Image, we will get the hospital name: ```Lenox Hill Hospital```

![image](https://github.com/Yazan03/Priv/assets/94278827/a169abf4-be1a-495c-ac98-980d02658943)

Combined everything together to get the flag. 

![image](https://github.com/Yazan03/Priv/assets/94278827/5fcb1561-fe56-4e1e-833f-0a2d5ef03204)






=============================================================================================================================

***Last challenge :***

With First blood !

![image](https://github.com/Yazan03/Priv/assets/94278827/9b0611bd-7779-4cc1-b334-f402219871a8)

We are given a hash, and the flag is the cleartext of the password. The goal is to make a specific list for ```irirs```, Let's get back to her IG. We will notice some pisces we can get to help us:

![image](https://github.com/Yazan03/Priv/assets/94278827/68cfd437-394f-4e0a-b649-aec9b936f715)
![image](https://github.com/Yazan03/Priv/assets/94278827/93168130-838c-4f04-951d-a2eb8b2027da)
![image](https://github.com/Yazan03/Priv/assets/94278827/66866e4b-e4ab-4f6b-8b3b-e62ceaaeb3ac)


Her mom's date is from her Facebook: 

![image](https://github.com/Yazan03/Priv/assets/94278827/d4855dd3-1066-420d-baa3-f1b6ecf368fc)

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
