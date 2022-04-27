
from datetime import datetime
import os
import json
import random
from time import sleep
from requests_oauthlib import OAuth1Session

how_much_to_spam = 50


def main():
    print(datetime.now())

    consumer_key = os.environ.get("CONSUMER_KEY")
    consumer_secret = os.environ.get("CONSUMER_SECRET")
    # print("Test")

    payload = string_define()

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
        
        if clock == '01:00' or clock == '10:00' or clock == '13:00' or clock == '18:00':
            while (0 < how_much_to_spam):
                # Making the request
                payload = string_define()
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
        elif clock == '01:01' or clock == '10:01' or clock == '13:01' or clock == '18:01':
            how_much_to_spam = holder
                
        if status == 0:
            print("Started the loop")
            status = 1

def string_define():
    current_time = datetime.now()
    msg = "Be sure to donate to Purdue ACM SIGBots for #PurdueDayOfGiving! I uniquely tweeted at " + str(current_time) + "!" 
    payload = {"text": msg}
    # sleep(60)
    return payload

if __name__ == "__main__":
    main()

