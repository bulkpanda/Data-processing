import json
import pandas as pd
def task2():
    review_path = 'course/data/a1/reviews/HealthStory.json'
    file = open(review_path)
    reviews = json.load(file)
    df_rows = []
    for review in reviews:
        num_satisfactory = 0
        news_id = review['news_id']
        news_title = review['original_title']
        review_title = review['title']
        rating = review['rating']
        #print(news_id)
        for seq in review['criteria']:
            if seq['answer'].lower() == 'satisfactory':
                num_satisfactory+=1
        df_rows.append({
            'news_id': news_id,
            'news_title': news_title,
            'review_title': review_title,
            'rating': rating,
            'num_satisfactory': num_satisfactory
        })

    df = pd.DataFrame(df_rows)
    df.set_index('news_id', inplace=True)
    print(df.head(5))
    df.to_csv('task2.csv')
    
task2()
