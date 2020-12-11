
print(Samples)
print(SynthDefs)

p1 >> play('Hello, I am so glad you are here')
p2 >> star([2, 5, 6])

import requests
import yaml
import pandas as pd


def get_bearer_token():
    with open("/Users/jgarson/config.yaml", "r") as f:
        s = yaml.safe_load(f)
    return s["recent_search"]["bearer_token"]


def make_headers(bearer_token):
    return {"Authorization": "Bearer {}".format(bearer_token)}


def make_a_request(headers):
    url = "https://api.twitter.com/2/tweets/search/recent?max_results=100&query=to:JessicaGarson"
    return requests.request("GET", url, headers=headers).json()


def create_dataframe(response):
    return pd.DataFrame(response['data'])
    

def parse_tweet(df):
    tweet = df['text'].iloc[1]
    word = tweet.lower()
    return word[15:]

# @jessicagarson hi, hello, or yo
def music_logic(word):
    options = [play("oxxxooo"), play("bbb"), bug(6), saw([1, 5, 2])]
    if word == "hello":
        return options[0]
    elif word == "hi":
        return options[1]
    elif word == "yo":
        return options[2]
    else:
        return options[3]


def main_logic():
    bearer_token = get_bearer_token()
    headers = make_headers(bearer_token)
    response = make_a_request(headers)
    df = create_dataframe(response)
    print(df)
    word = parse_tweet(df)
    p1 >> music_logic(word)

main_logic()

a1 >> play('sgs')
a2 >> play('thanks for joining today')
a3 >> play('Thanks again!')
