﻿# Programming-note

1. Download google drive file
```shell
wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=0BwmD_VLjROrfTHk4NFg2SndKcjQ' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=0BwmD_VLjROrfTHk4NFg2SndKcjQ" -O cnn_stories.tgz && rm -rf /tmp/cookies.txt
```
