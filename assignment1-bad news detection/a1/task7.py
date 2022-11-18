import numpy as np
import json
import pandas as pd
import matplotlib.pyplot as plt
import math

def task7():

    df = pd.read_csv('task2.csv')
    file = open('task6.json')
    word_dict = json.load(file)

    rating_dict = {}
    tot_real = 0
    tot_fake = 0

    for news in df['news_id']:
        rating = df.loc[df['news_id'] == news, 'rating'].values[0]
        if rating < 3:
            rating_dict[news] = 'fake'
            tot_fake += 1
        else:
            rating_dict[news] = 'real'
            tot_real += 1

    real_dict = {}
    fake_dict = {}
    log_odd_df = []

    # 1263 => no word appears in all articles

    for word, news in word_dict.items():
        if len(news) >= 10:
            nreal = 0
            nfake = 0
            for n in news:
                if rating_dict[n] == 'real':
                    nreal += 1
                if rating_dict[n] == 'fake':
                    nfake += 1
            preal = nreal/tot_real
            pfake = nfake/tot_fake
            real_dict[word] = preal
            fake_dict[word] = pfake
            if (preal != 0 and preal != 1) and (pfake != 0 and pfake != 1):
                real_odds = preal/(1-preal)
                fake_odds = pfake/(1-pfake)
                odd_ratio = fake_odds/real_odds
                log_odd_ratio = math.log10(odd_ratio)

                log_odd_df.append(
                    {
                        'word': word,
                        'log_odds_ratio': log_odd_ratio
                    }
                )

    output = pd.DataFrame(log_odd_df)

    output.to_csv('task7a.csv')
    log_odds_ratio = output['log_odds_ratio'].values

    plt.hist(log_odds_ratio, bins = 20, ec="k")
    plt.title('Distribution of log odds ratio')
    plt.xlabel('Log odd value')
    plt.savefig('task7b.png')
    plt.show()

    df1 = output.sort_values('log_odds_ratio', ascending=True)
    low15 = df1[0:15]     # lowest 15 for fake news
    lowoddratio = np.array(low15['log_odds_ratio'].values)

    lowoddratio = 10**lowoddratio


    df2 = output.sort_values('log_odds_ratio', ascending=False)
    top15 = df2[0:15]  # lowest 15 for fake news
    topoddratio = np.array(top15['log_odds_ratio'].values)

    topoddratio = 10 ** topoddratio


    fig, ax = plt.subplots(1,2,figsize=(10, 8))
    ax[0].bar(low15['word'].values, lowoddratio, align='center')
    ax[0].set_xticklabels(low15['word'].values, rotation=90, fontsize=7)
    ax[0].set_ylabel('Odds ratio')
    ax[0].set_title('Lowest 15 odds ratio words for fake news')

    ax[1].bar(top15['word'].values, topoddratio, align='center')
    ax[1].set_xticklabels(top15['word'].values, rotation=90, fontsize=7)
    ax[1].set_title('Top 15 odds ratio words for fake news')
    plt.savefig('task7c.png')
    plt.show()


task7()