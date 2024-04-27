# TwitterSpamBot
Originally made for Purdue ACM SIGBots, April 2022.

## A Note On Longevity
This will still send messages to an X account. However, since Musk has purchased the platform, the amount you can spam the platform with messages such as this is extremely limited, and the code will result in an error when you try to run it as is.

You are welcome to reference the code as much as you would like for a non-spamming X API, but this code no longer works for it's intended purpose as of 2024.

## Operational Notes

1. You're going to have to create a Twitter account that's been approved for developer mode WITH elevated permission levels.
2. I would advise that you leave the how_much_to_spam at 50 or lower so that your Twitter account doesn't get flagged as a spam bot. 50 itself may be too high, I don't know. This variable is declared on line 9.
3. To keep this from looking like a bot, ideally you should change up the message a little bit. An important note on the date is that TWITTER DOES NOT ALLOW BOT CREATION OF IDENTICAL POSTS. You need some aspect that will change. I would recommend leaving the date string that I added as default, but one could also add incrementing numbers, randomly generated large numbers, or something else that would ensure any message added is unique. The message is changable on line 97.
4. This bot HAS to be started at least 1 minute before your desired operation time. Twitter requires an authentication step for simple bots, and this project simply isn't worth my time to try to find a way around it as I only plan to use it once. There is a possibility I'll modify it for permanent use, but it's unlikely.
5. As this bot is constantly running to check for 1am, 10am, 1pm, and 6pm, it doesn't actually end on it's own. You can kill it with **Control + F**.

For reference, Twitter Developer will call your some of your keys "API Keys." This is the same as a "Consumer Key", and same principle applies to the secret version of both.

How to actually use this:

I'd personally recommend writing a .command script for this, but I didn't upload mine to GitHub as I don't want to reveal my keys. Basically, you need to run these three commands in a terminal window.

_export 'CONSUMER_KEY'='_<place consumer/api key here>_'_

_export 'CONSUMER_SECRET'=_'<place consumer/api secret key here>'
  
_python3 TwitterSpamBot.py_
  
## Requires Python Packages
- datetime
- requests_oauthlib
- time
- json
- os
