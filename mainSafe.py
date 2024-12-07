from openai import OpenAI
from afinn import Afinn
import nltk
import pandas as pd

nltk.download('punkt')
nltk.download('punkt_tab')

client = OpenAI(api_key = "abc")

df = pd.read_csv("BuzzFeed_fake_news_content.csv")
df = df[df['text'].notna() & df['text'].str.strip().astype(bool)]

#Afinn

afinn = Afinn(emoticons = True)

def calculate_sentiment(article_text):
    sentences = nltk.sent_tokenize(article_text)
    sentiment_scores = [afinn.score(sentence) for sentence in sentences]
    
    overall_sentiment = sum(sentiment_scores)
    average_sentiment = overall_sentiment / len(sentences) if sentences else 0
    total_words = len(nltk.word_tokenize(article_text))
    average_sentiment_per_word = overall_sentiment / total_words if total_words > 0 else 0

    return overall_sentiment, average_sentiment, average_sentiment_per_word, total_words

#Generate bullet points

def get_bullet_points(article_text):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a professional bullet point summarizer."},
                {"role": "user", "content": f"Summarize the following news article into bullet points. Rely strictly on the provided text, without including external information.:\n\n{article_text}"}
            ],
            temperature = 1
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error processing  article: {e}")
        return "Error: Unable to generate bullet points."

#Generate new news article

def generate_article_from_bullets(bullet_points, nb_words):
    try:
        reponse = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a news article writer."},
                {"role": "user", "content": f"Your boss has asked you to write a news article of about {nb_words} words long, based only on the bullet points, without referencing or including any information outside of the bullet points.\n\n{bullet_points}"}
            ],
            temperature = 1
        )
        return reponse.choices[0].message.content
    except Exception as e:
        print(f"Error processing article: {e}")
        return "Error: Unable to generate new article."

#Dataset entry into system

article_column = 'text'

df['bullet_points'] = ""
df['generated_article'] = ""
df['original_sentiment'] = 0.0
df['generated_sentiment'] = 0.0

for i in range(len(df)):
    article_text = df.loc[i, article_column]

    if pd.isna(article_text):
        print(f"Skipping row {i} due to NaN value.")
        continue

    total_words = len(nltk.word_tokenize(article_text))

    bullet_points = get_bullet_points(article_text)
    df.loc[i, 'bullet_points'] = bullet_points

    generated_article = generate_article_from_bullets(bullet_points, total_words)
    df.loc[i, 'generated_article'] = generated_article

    original_sentiment, avg_sentiment, avg_sentiment_per_word, total_words = calculate_sentiment(article_text)
    df.loc[i, 'num_words'] = total_words
    df.loc[i, 'original_sentiment'] = original_sentiment
    df.loc[i, 'avg_sentiment_per_sen'] = avg_sentiment
    df.loc[i, 'avg_sentiment_per_word'] = avg_sentiment_per_word

    generated_sentiment, avg_gen_sentiment, avg_gen_sentiment_per_word, total_words = calculate_sentiment(generated_article)
    df.loc[i, 'num_words_gen'] = total_words
    df.loc[i, 'generated_sentiment'] = generated_sentiment
    df.loc[i, 'avg_gen_sentiment_per_sen'] = avg_gen_sentiment
    df.loc[i, 'avg_gen_sentiment_per_word'] = avg_gen_sentiment_per_word

    #Save each iteration
    print("article " + str(i))
    df.to_csv("GEN_BuzzFeed_fake_news_temp1_ite5.csv", index=False)

print('\a')

