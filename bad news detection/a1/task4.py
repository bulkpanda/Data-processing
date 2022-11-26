import json
import pandas as pd
import matplotlib.pyplot as plt
def task4():
    review_path = 'course/data/a1/reviews/HealthStory.json'
    file = open(review_path)
    reviews = json.load(file)
    num_articles = {}
    rating = {}
    for review in reviews:
        if review['news_source'] is not None and review['news_source'] != '':
            if review['news_source'] in num_articles.keys():
                num_articles[review['news_source']] += 1
                rating[review['news_source']] += review['rating']
            else:
                num_articles[review['news_source']] = 1
                rating[review['news_source']] = review['rating']

    for key in num_articles.keys():
        rating[key] = rating[key]/num_articles[key]
    print(num_articles)
    print(rating)
    df = pd.DataFrame(columns = ['news_source','num_articles','avg_rating'])
    df['news_source'] = rating.keys()
    df['num_articles'] = num_articles.values()
    df['avg_rating'] = rating.values()
    print(df)
    df.to_csv('task4a.csv')
    df = df.sort_values('avg_rating', ascending=False)
    graph = {}
    for i in df.index:
        if df['num_articles'][i]>=5:
            graph[df['news_source'][i]] = df['avg_rating'][i]
    print(graph)
    plt.bar(range(len(graph)), list(graph.values()), align='center')
    plt.xticks(range(len(graph)), list(graph.keys()), rotation=90, fontsize=7)
    plt.ylabel('Average rating')
    plt.title('Ratings of news sources')
    plt.savefig('task4b.png',bbox_inches = "tight")
    plt.show()
task4()