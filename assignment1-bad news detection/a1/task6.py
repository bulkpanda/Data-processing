import os
import json
import re
from nltk.corpus import stopwords
import nltk
#nltk.download('stopwords')
#nltk.download('punkt')

def task6():
    content_path = 'course/data/a1/content/HealthStory'
    content_items = os.listdir(content_path)
    stop_words = set(stopwords.words('english'))
    stop_words.add('')
    word_dict = {}
    for item in content_items:
        news_id = item.split('.')[0]
        file = open(content_path+'/'+item)
        data = json.load(file)
        text = data['text']
        text = re.sub(r'[^A-Za-z\s]', ' ', text)
        text = re.sub(r'\s+', ' ', text)
        text = text.lower()
        tokens = text.split(' ')
        no_stopwords = [w for w in tokens if not w in stop_words]
        no_stopwords = set(no_stopwords)

        for word in no_stopwords:
            if word in word_dict.keys():
                word_dict[word].append(news_id)
            else:
                word_dict[word] = [news_id]
    with open("task6.json", "w") as outfile:
        json.dump(word_dict, outfile)
task6()