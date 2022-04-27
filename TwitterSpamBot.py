
from datetime import datetime
import os
import json
import random
from time import sleep
from requests_oauthlib import OAuth1Session



def main():
    how_much_to_spam = 100
    print(datetime.now())

    consumer_key = os.environ.get("CONSUMER_KEY")
    consumer_secret = os.environ.get("CONSUMER_SECRET")
    # print("Test")

    # payload = string_define()

    # Get request token
    request_token_url = "https://api.twitter.com/oauth/request_token?oauth_callback=oob&x_auth_access_type=write"
    oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

    try:
        fetch_response = oauth.fetch_request_token(request_token_url)
    except ValueError:
        print(
            "There may have been an issue with the consumer_key or consumer_secret you entered."
        )

    resource_owner_key = fetch_response.get("oauth_token")
    resource_owner_secret = fetch_response.get("oauth_token_secret")
    print("Got OAuth token: %s" % resource_owner_key)

    # Get authorization
    base_authorization_url = "https://api.twitter.com/oauth/authorize"
    authorization_url = oauth.authorization_url(base_authorization_url)
    print("Please go here and authorize: %s" % authorization_url)
    verifier = input("Paste the PIN here: ")

    # Get the access token
    access_token_url = "https://api.twitter.com/oauth/access_token"
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=resource_owner_key,
        resource_owner_secret=resource_owner_secret,
        verifier=verifier,
    )
    oauth_tokens = oauth.fetch_access_token(access_token_url)

    access_token = oauth_tokens["oauth_token"]
    access_token_secret = oauth_tokens["oauth_token_secret"]

    # Make the request
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    )

    looper = 0
    status = 0
    holder = how_much_to_spam
    while looper < 5:
        current_time = str(datetime.now())
        clock = current_time[11:16]
        if clock == '01:00' or clock == '10:00' or clock == '13:00' or clock == '18:00' or clock == '14:10':
            while (how_much_to_spam > 0):
                # Making the request
                payload = string_define(how_much_to_spam)
                response = oauth.post(
                    "https://api.twitter.com/2/tweets",
                    json=payload,
                )

                if response.status_code != 201:
                    raise Exception(
                        "Request returned an error: {} {}".format(response.status_code, response.text)
                    )

                print("Response code: {}".format(response.status_code))

                # Saving the response as JSON
                json_response = response.json()
                print(json.dumps(json_response, indent=4, sort_keys=True))
                how_much_to_spam = how_much_to_spam - 1
        elif clock == '1:01' or clock == '10:01' or clock == '13:01' or clock == '18:01':
            how_much_to_spam = holder

                
        if status == 0:
            print("Started the loop")
            status = 1

def string_define(num):
    
    # current_time = datetime.now()
    cased_msg = {
        50 : "We'll stay away from Johnny Depp topics for the rest of this. He's kind of controversial right now and not particularly relevant to the robotics or Purdue community.",
        49 : "We're pretty sure we actually got the 50th tweet at both 10am, and 1pm, but maybe that's not unique enough for Purdue's standards",
        48 : "Which is our only guess as to why they're picking tweets that actually happened after the 50th original tweet",
        47 : "By all accounts, we're confused.",
        46 : "We have Bob the Builder themed bots this year",
        45 : "We're going to the VEX world championship next week",
        44 : "We develop an educational robot operating system",
        43 : "We run a wiki that educates people on robotics",
        42 : "I still think we should've named a bot 'Pilchard the Cat', but whatever.",
        41 : "Our President is Micah Rassi, so if you're interested in joining reach out to him ig",
        40 : "Or really anyone on the team",
        39 : "Or even this bot, there's an actual human that looks at notifications for this account",
        38 : "Isn't that weird?",
        37 : "Writing 100 unique tweets is kinda hard",
        36 : "I'm at case statement 36",
        35 : "AND IT GOES DOWNWARD TO 0!",
        34 : "If you have nothing to do with Purdue, but like VEX, try PROS",
        33 : "COVID hit us hard financially so getting the 50th tweet would mean a lot",
        32 : "Despite that, our club has grown substantially!",
        31 : "I'm running out of ideas, so I'm just gonna spew off names of former presidents",
        30 : "President 2020-21: Chris Ridenour",
        29 : "President 2019-20: Joe Skowronski",
        28 : "President 2018-19: Lucas Baston",
        27 : "President 2017-18: Jonathan Bayless",
        26 : "Wait, spewing off previous presidents may not be unique enough.",
        25 : "We'd like to thank our alumni for support, financial and non-financial",
        24 : "Including but not limited to: Javid Habibi",
        23 : "Jonathan Bayless",
        22 : "Hotel",
        21 : "Stephen Carlson",
        20 : "We're not going to buy Will any more ranch with donated funds, we promise.",
        19 : "We promise not to delete PROS",
        18 : "What else am I supposed to write here?",
        17 : "If you have any sponsorship questions, please reach out to AR Miller, our treasurer for the 2021-22 season",
        16 : "We advise against petting the bots like a dog",
        15 : "I only have to write fifteen more of these",
        14 : "By the way, if you're seeing this not at 6pm, I'm just testing the system",
        13 : "Bingus bongus our best bot was big chungus",
        12 : "We had a season where we named the bots after Waffle House founders and songs",
        11 : "If you donate enough money we'll name the bot after you.",
        10 : "We can also name a fake-memorial competition after you and get emails about people who are sad about your passing despite the fact you're still alive",
        9 : "True story.",
        8 : "Bot bot bot bot bot bot bot bot bot",
        7 : "Vex is superior to first change my mind",
        6 : "If anyone still uses the Atom version of PROS I'm so sorry",
        5 : "Water game?",
        4 : "We're gonna use 393s next year and VEX corporate can't stop us.",
        3 : "2023 Cortex Season",
        2 : "Oh, and if you're still paying attention, I lost the game",
        1 : "I hope this about does it. Maybe one of these was 50th. Thank you.",
        100: "I'm gonna do even more tweets this time, but at least they won't just be the same message and the time",
        99: "We were told we were allowed to use a bot for this, so here we go!",
        98: "Tweet one! This is not a bot!",
        97: "Tweedle dee tweetle dum! We'll make a reveal video when we get off our bums!",
        96: "I wonder who is reading this? Would you like to know about our robots?",
        95: "Unfortunately, this is just going to be a bunch of sarcastic messages",
        94: "I am unbelievably sorry.",
        93: "We do VEX Robotics and have been since the early 2010s",
        92: "We've gone to VEX Worlds every year... excluding COVID",
        91: "We're consistently one of the top ranked VEX U teams globally",
        90: "We bring in a lot of revenue for Purdue but I don't think the people in Hovde realize that",
        89: "That's neither here nor there",
        88: "We're consistently featured in the exponent,",
        87: "This bot was really easy to code I'm surprised more student orgs don't do it",
        86: "If this gets ten retweets we'll name our main bots Steve 1 and Steve 2 next season.",
        85: "That is a promise.",
        84: "Buy our merch! We don't have any!",
        83: "I'm really just procrastinating finishing my ASIC design lab by coding this.",
        82: "my team's demo is tomorrow and honestly my test benches aren't working yet so I'm kinda mortified",
        81: "It'll be okay though",
        80: "I think. Maybe.",
        79: "I really hope people are reading this in the correct order. That'd be weird if they weren't.",
        78: "Is this 'original' enough for you, bursar?",
        77: "*i'm sorry bursar i repent pls be nice*",
        76: "If none of these are deemed the 50th tweet I'm gonna go to Harry's and order 3 Baltimore Zoos.",
        75: "I wrote the latter half of this bot first, so in case you can't tell, I'm like, majorly out of ideas",
        74: "Download PROS!",
        73: "I feel like I'm writing the Minecraft splash screens? Y'know?",
        72: "Idk if I said this anywhere but I implore anyone reading this to donate",
        71: "Please",
        70: "Pretty, pretty, pretty please.",
        69: "This is case statement 69. Nice.",
        68: "Lack of professionalism aside, we do genuinely good work for the robotics education community",
        67: "And any small donation would massively impact not only us but other universities, as well as high school and middle school students.",
        66: "While our bots only do real educational benefit for us, the knowledge required for those bots go onto our Wiki, which is used by thousands daily",
        65: "This wiki allows other kids and adults alike to build their own robots.",
        64: "That's not to mention our PROS operating system. That takes a lot of work to upkeep, and a lot of it cannot be done withhout fiscal assistance",
        63: "We'll name a robot after you if that's what it takes",
        62: "If your name is Jeff, we'll be sure to name our robot Jeff",
        61: "Actually, we'll name the bot anything you want. Not just Jeff, or Steve 1 and Steve 2.",
        60: "But that's neither here nor there. I'm just saying for the right price we'll give you naming rights",
        59: "If you give us 6 figures we'll change our team initials to JEFF.",
        58: "Purdue probably won't like that very much, so if you're thinking of making a six figure donation, please do it in two smaller sums",
        57: "What am I talking about, nobody is going to do that",
        56: "So how about that airline food?",
        55: "Ha ha ha, right?",
        54: "Hello? Anybody?",
        53: "I really hope this is the 50th tweet so that it is all worth it",
        52: "This feels like offbrand Charlie and the Chocolate Factory",
        51: "Except this has less Johnny Depp and more student debt."

    }

    msg = cased_msg[num] + " #PurdueACMSigBots #PurdueDayOfGiving"
    payload = {"text": msg}
    # sleep(60)
    return payload

if __name__ == "__main__":
    main()

