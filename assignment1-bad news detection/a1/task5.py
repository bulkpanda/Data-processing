import json
import pandas as pd
import matplotlib.pyplot as plt
def task5():
    tweet_path = 'course/data/a1/engagements/HealthStory.json'
    review_path = 'course/data/a1/reviews/HealthStory.json'

    file1 = open(tweet_path)
    stories = json.load(file1)

    file2 = open(review_path)
    reviews = json.load(file2)

    popularity = {}
    rating = {}
    for id, tweet in stories.items():
        tweet_list = []
        for key, item in tweet.items():
            tweet_list = tweet_list + item
        num_tweets = len(set(tweet_list))
        popularity[id] = num_tweets
    #print(popularity)

    for review in reviews:
        rating[review['news_id']] = review['rating']
    #print(rating)

    num_article_per_rating = {}
    for i in range(0,6):
        num_article_per_rating[i] = list(rating.values()).count(i)
    print(num_article_per_rating)

    rating_pop = {}

    for key in popularity.keys():
        if rating[key] in rating_pop.keys():
            rating_pop[rating[key]] += popularity[key]
        else:
            rating_pop[rating[key]] = popularity[key]

    for key in rating_pop.keys():
        rating_pop[key] = rating_pop[key]/num_article_per_rating[key]
    #print(rating_pop)

    rating_pop_list = []
    for i in range(6):
        rating_pop_list.append(rating_pop[i])
    print(rating_pop_list)

    plt.bar(range(len(rating_pop_list)), rating_pop_list, align='center')
    plt.xticks(range(len(rating_pop)), [0,1,2,3,4,5])
    plt.ylabel('Popularity(Average number of tweets)')
    plt.xlabel('Rating')
    plt.title('Popularity v/s Rating')
    plt.savefig('task5.png', bbox_inches="tight")
    plt.show()
task5()