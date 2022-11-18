import os
import json

def task1():
    content_path = 'course/data/a1/content/HealthStory'
    review_path = 'course/data/a1/reviews/HealthStory.json'
    tweet_path = 'course/data/a1/engagements/HealthStory.json'

    content_items = os.listdir(content_path)
    X = len(content_items)
    # print(f'Number of articles:{X}')

    file = open(review_path)
    reviews = json.load(file)
    Y = len(reviews)
    # print(f'Number of reviews:{Y}')

    file = open(tweet_path)
    tweets = json.load(file)
    tweet_list = []
    for id,tweet in tweets.items():
        for key, item in tweet.items():
            tweet_list = tweet_list + item
    tweet_list_unique = set(tweet_list)
    # print(len(tweet_list))
    Z = len(tweet_list_unique)
    # print(f'Number of tweets: {Z}')

    json_data = {"Total number of articles": X, "Total number of reviews": Y, "Total number of tweets": Z}
    with open("task1.json", "w") as outfile:
        json.dump(json_data, outfile)


