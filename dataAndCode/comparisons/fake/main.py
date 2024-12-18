import pandas as pd

df = pd.read_csv("BuzzFeed_fake_news_content.csv")
df = df[df['text'].notna() & df['text'].str.strip().astype(bool)]

df1 = pd.read_csv("BuzzFeed_fake_news_with_averages_temp0.csv")
df2 = pd.read_csv("BuzzFeed_fake_news_with_averages_temp0.5.csv")
df3 = pd.read_csv("BuzzFeed_fake_news_with_averages_temp1.csv")

df['original_sentiment'] = None
df['num_words'] = None
df['avg_sentiment_per_sen'] = None
df['avg_sentiment_per_word'] = None

df['avg_generated_sentiment_temp0'] = None
df['avg_num_words_gen_temp0'] = None
df['avg_gen_sentiment_per_sen_temp0'] = None
df['avg_gen_sentiment_per_word_temp0'] = None

df['avg_generated_sentiment_temp0.5'] = None
df['avg_num_words_gen_temp0.5'] = None
df['avg_gen_sentiment_per_sen_temp0.5'] = None
df['avg_gen_sentiment_per_word_temp0.5'] = None

df['avg_generated_sentiment_temp1'] = None
df['avg_num_words_gen_temp1'] = None
df['avg_gen_sentiment_per_sen_temp1'] = None
df['avg_gen_sentiment_per_word_temp1'] = None

rows_to_delete = []

for i in range(len(df1)):
    if df1.loc[i, "num_words"] < 100 or df1.loc[i, "num_words"] > 1200:
        rows_to_delete.append(i)

    df.loc[i, 'original_sentiment'] = df1.loc[i, "original_sentiment"]
    df.loc[i, 'num_words'] = df1.loc[i, "num_words"]
    df.loc[i, 'avg_sentiment_per_sen'] = df1.loc[i, "avg_sentiment_per_sen"]
    df.loc[i, 'avg_sentiment_per_word'] = df1.loc[i, "avg_sentiment_per_word"]

    df.loc[i, 'avg_generated_sentiment_temp0'] = df1.loc[i, "avg_generated_sentiment"]
    df.loc[i, 'avg_num_words_gen_temp0'] = df1.loc[i, "avg_num_words_gen"]
    df.loc[i, 'avg_gen_sentiment_per_word_temp0'] = df1.loc[i, "avg_gen_sentiment_per_word"]
    df.loc[i, 'diff_sentiment_temp0'] = abs(df.loc[i, 'avg_sentiment_per_word'] - df.loc[i, 'avg_gen_sentiment_per_word_temp0'])

    df.loc[i, 'avg_generated_sentiment_temp0.5'] = df2.loc[i, "avg_generated_sentiment"]
    df.loc[i, 'avg_num_words_gen_temp0.5'] = df2.loc[i, "avg_num_words_gen"]
    df.loc[i, 'avg_gen_sentiment_per_word_temp0.5'] = df2.loc[i, "avg_gen_sentiment_per_word"]
    df.loc[i, 'diff_sentiment_temp0.5'] = abs(df.loc[i, 'avg_sentiment_per_word'] - df.loc[i, 'avg_gen_sentiment_per_word_temp0.5'])


    df.loc[i, 'avg_generated_sentiment_temp1'] = df3.loc[i, "avg_generated_sentiment"]
    df.loc[i, 'avg_num_words_gen_temp1'] = df3.loc[i, "avg_num_words_gen"]
    df.loc[i, 'avg_gen_sentiment_per_word_temp1'] = df3.loc[i, "avg_gen_sentiment_per_word"]
    df.loc[i, 'diff_sentiment_temp1'] = abs(df.loc[i, 'avg_sentiment_per_word'] - df.loc[i, 'avg_gen_sentiment_per_word_temp1'])


columns_to_remove = [
    'avg_sentiment_per_sen',
    'avg_gen_sentiment_per_sen_temp0', 
    'avg_gen_sentiment_per_sen_temp0.5', 
    'avg_gen_sentiment_per_sen_temp1'
]


df = df.drop(rows_to_delete).reset_index(drop=True)
df = df.drop(columns=columns_to_remove)
df.to_csv("BuzzFeed_fake_news_grouped_temp_data2.csv", index=False)
