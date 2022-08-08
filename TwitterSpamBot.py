
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
            # Currently only built to support the hard-coded messages.
            while (how_much_to_spam > 0):
                # Making the request
                payload = predefined_strings(how_much_to_spam)
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

# This option is used if you're trying to Tweet specific messages.
# Currently there is capability for 100.
# The sentences have to be hard-coded.
def predefined_strings(num):
    cased_msg = {
        50 : "Sentence 50.",
        49 : "Sentence 49.",
        48 : "Sentence 48.",
        47 : "Sentence 47.",
        46 : "Sentence 46.",
        45 : "Sentence 45.",
        44 : "Sentence 44.",
        43 : "Sentence 43.",
        42 : "Sentence 42.",
        41 : "Sentence 41.",
        40 : "Sentence 40.",
        39 : "Sentence 39.",
        38 : "Sentence 38.",
        37 : "Sentence 37.",
        36 : "Sentence 36.",
        35 : "Sentence 35.",
        34 : "Sentence 34.",
        33 : "Sentence 33.",
        32 : "Sentence 32.",
        31 : "Sentence 31.",
        30 : "Sentence 30.",
        29 : "Sentence 29.",
        28 : "Sentence 28.",
        27 : "Sentence 27.",
        26 : "Sentence 26.",
        25 : "Sentence 25.",
        24 : "Sentence 24.",
        23 : "Sentence 23.",
        22 : "Sentence 22.",
        21 : "Sentence 21.",
        20 : "Sentence 20.",
        19 : "Sentence 19.",
        18 : "Sentence 18.",
        17 : "Sentence 17.",
        16 : "Sentence 16.",
        15 : "Sentence 15.",
        14 : "Sentence 14.",
        13 : "Sentence 13.",
        12 : "Sentence 12.",
        11 : "Sentence 11.",
        10 : "Sentence 10.",
        9 : "Sentence 9.",
        8 : "Sentence 8.",
        7 : "Sentence 7.",
        6 : "Sentence 6.",
        5 : "Sentence 5.",
        4 : "Sentence 4.",
        3 : "Sentence 3.",
        2 : "Sentence 2.",
        1 : "Sentence 1.",
        100: "Sentence 100.",
        99: "Sentence 99.",
        98: "Sentence 98.",
        97: "Sentence 97.",
        96: "Sentence 96.",
        95: "Sentence 95.",
        94: "Sentence 94.",
        93: "Sentence 93.",
        92: "Sentence 92.",
        91: "Sentence 91.",
        90: "Sentence 90.",
        89: "Sentence 89.",
        88: "Sentence 88.",
        87: "Sentence 87.",
        86: "Sentence 86.",
        85: "Sentence 85.",
        84: "Sentence 84.",
        83: "Sentence 83.",
        82: "Sentence 82.",
        81: "Sentence 81.",
        80: "Sentence 80.",
        79: "Sentence 79.",
        78: "Sentence 78.",
        77: "Sentence 77.",
        76: "Sentence 76.",
        75: "Sentence 75.",
        74: "Sentence 74.",
        73: "Sentence 73.",
        72: "Sentence 72.",
        71: "Sentence 71.",
        70: "Sentence 70.",
        69: "Sentence 69 (nice).",
        68: "Sentence 68.",
        67: "Sentence 67.",
        66: "Sentence 66.",
        65: "Sentence 65.",
        64: "Sentence 64.",
        63: "Sentence 63.",
        62: "Sentence 62.",
        61: "Sentence 61.",
        60: "Sentence 60.",
        59: "Sentence 59.",
        58: "Sentence 58.",
        57: "Sentence 57.",
        56: "Sentence 56.",
        55: "Sentence 55.",
        54: "Sentence 54.",
        53: "Sentence 53.",
        52: "Sentence 52.",
        51: "Sentence 51."

    }

    # Used to add standard hashtags to every message.
    msg = cased_msg[num] + " #optionalhashtag1 #optionalhashtag2"
    payload = {"text": msg}
    return payload

if __name__ == "__main__":
    main()

