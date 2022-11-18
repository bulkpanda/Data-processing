import os
import json
import datetime
import pandas as pd
import matplotlib.pyplot as plt
def task3():
    content_path = 'course/data/a1/content/HealthStory'
    content_items = os.listdir(content_path)
    df_rows = []
    for item in content_items:
        file = open(content_path+'/'+item)
        data = json.load(file)
        news_id = item.split('.')[0]
        #print(news_id)
        if data['publish_date'] is not None:
            date_time = datetime.datetime.fromtimestamp(data['publish_date'])
            month = date_time.month
            day = date_time.day
            year = date_time.year
        else:
            month = None
            day = None
            year = None
        #print(year, month, day)
        df_rows.append({
            'news_id':news_id,
            'year': year,
            'month': month,
            'day': day
        })
    df = pd.DataFrame(df_rows)
    df.to_csv('task3a.csv')
    yearcount={}
    for i in range(int(min(df['year'])), int(max(df['year'])+1)):
        yearcount[i] = list(df['year']).count(i)

    def addlabels(x, y):
        for i in range(len(x)):
            plt.text(i, y[i]+2, y[i], ha='center')


    print(yearcount)
    plt.bar(range(len(yearcount)), list(yearcount.values()), align = 'center')
    plt.xticks(range(len(yearcount)), list(yearcount.keys()))
    addlabels(list(yearcount.keys()), list(yearcount.values()))
    plt.xlabel('Year')
    plt.ylabel('Number of articles')
    plt.title('Number of articles v/s year')
    plt.savefig('task3b.png')
    plt.show()

task3()