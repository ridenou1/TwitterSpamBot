# TwitterSpamBot
Some notes on operation:

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
  
If you have any questions, please feel free to @ me in the Discord. I'll be making this repo private after Wednesday.
