import pandas as pd


df = pd.read_csv("BuzzFeed_real_news_content.csv")
df = df[df['text'].notna() & df['text'].str.strip().astype(bool)]
df1 = pd.read_csv("GEN_BuzzFeed_real_news_temp0.5_ite1.csv")
df2 = pd.read_csv("GEN_BuzzFeed_real_news_temp0.5_ite2.csv")
df3 = pd.read_csv("GEN_BuzzFeed_real_news_temp0.5_ite3.csv")
df4 = pd.read_csv("GEN_BuzzFeed_real_news_temp0.5_ite4.csv")
df5 = pd.read_csv("GEN_BuzzFeed_real_news_temp0.5_ite5.csv")

df['original_sentiment'] = None
df['num_words'] = None
df['avg_sentiment_per_sen'] = None
df['avg_sentiment_per_word'] = None
df['avg_generated_sentiment'] = None
df['avg_num_words_gen'] = None
df['avg_gen_sentiment_per_sen'] = None
df['avg_gen_sentiment_per_word'] = None

rows_to_delete = []

for i in range(len(df1)):
    if df1.loc[i, "num_words"] < 100:
        rows_to_delete.append(i)
    
    df.loc[i, 'original_sentiment'] = df1.loc[i, "original_sentiment"]
    df.loc[i, 'num_words'] = df1.loc[i, "num_words"]
    df.loc[i, 'avg_sentiment_per_sen'] = df1.loc[i, "avg_sentiment_per_sen"]
    df.loc[i, 'avg_sentiment_per_word'] = df1.loc[i, "avg_sentiment_per_word"]
    df.loc[i, 'avg_generated_sentiment'] = (df1.loc[i, 'generated_sentiment'] + df2.loc[i, 'generated_sentiment'] + df3.loc[i, 'generated_sentiment'] + df4.loc[i, 'generated_sentiment'] + df5.loc[i, 'generated_sentiment'])/5.0
    df.loc[i, 'avg_num_words_gen'] = (df1.loc[i, 'num_words_gen'] + df2.loc[i, 'num_words_gen'] + df3.loc[i, 'num_words_gen'] + df4.loc[i, 'num_words_gen'] + df5.loc[i, 'num_words_gen'])/5
    df.loc[i, 'avg_gen_sentiment_per_sen'] = (df1.loc[i, 'avg_gen_sentiment_per_sen'] + df2.loc[i, 'avg_gen_sentiment_per_sen'] + df3.loc[i, 'avg_gen_sentiment_per_sen'] + df4.loc[i, 'avg_gen_sentiment_per_sen'] + df5.loc[i, 'avg_gen_sentiment_per_sen'])/5.0
    df.loc[i, 'avg_gen_sentiment_per_word'] = (df1.loc[i, 'avg_gen_sentiment_per_word'] + df2.loc[i, 'avg_gen_sentiment_per_word'] + df3.loc[i, 'avg_gen_sentiment_per_word'] + df4.loc[i, 'avg_gen_sentiment_per_word'] + df5.loc[i, 'avg_gen_sentiment_per_word'])/5.0

df = df.drop(rows_to_delete).reset_index(drop=True)
df.to_csv("BuzzFeed_real_news_with_averages_temp0.5.csv", index=False)
