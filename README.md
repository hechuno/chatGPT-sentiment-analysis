# Sentiment Analysis of Content Created by chatGPT

Under the supervision of Professor Raphaël Khoury, this is my final project to obtain my bachelor's in computer science from the University of Québec in Outaouais.

## Objective

More content is being written by chatGPT. Ideally, chatGPT would use language that is unbiased and factual. This research seeks to find if the content created by chatGPT is positive, neutral, or negative. In particular, if chatGPT has a bias towards certain subjects, and if/how much the temperature parameter affects the language used by chatGPT. We used the chatGPT 4o-mini model, and the chatGPT API to generate the data.

## Methodology

This project consists of two phases:
1. Data Preparation
2. Data Analysis and Interpretation

### 1. Data Preparation

#### 1.1 Find a database of news articles

We used the BuzzFeed real and fake news articles from the following database: https://www.kaggle.com/datasets/mdepak/fakenewsnet. We only kept articles over 100 words long.

#### 1.2 chatGPT Article Generation

Using the chatGPT API and the chatGPT model 4o-mini, we first asked chatGPT to summarize the original article using the following prompt:
```
{"role": "system", "content": "You are a professional bullet point summarizer."},
                {"role": "user", "content": f"Summarize the following news article into bullet points. Rely strictly on the provided text, without including external information.:\n\n{article_text}"}
```

We then asked chatGPT to generate a new article based only on the bullet points that it just generated, we made sure to do this in a new prompt, to ensure that it did not have access to the original article and only the bullet points. This gave freedom to chatGPT to choose what was important to include in the bullet points, and the freedom to interpret the bullet points without influence from the original article. The following prompt was used:

```
{"role": "system", "content": "You are a news article writer."},
                {"role": "user", "content": f"Your boss has asked you to write a news article of about {nb_words} words long, based only on the bullet points, without referencing or including any information outside of the bullet points.\n\n{bullet_points}"}
```

Use a sentimental analysis algorithm to generate a sentimental score that represents the positivity or negativity of the language used in original article and the generated article.

#### 1.3 Sentiment Score Generation

We used the sentiment analysis algorithm Afinn: https://github.com/fnielsen/afinn to generate the sentiment score for both the original articles and the generated articles. 
We kept track of the following parameters:
* original article sentiment score
* original article number of words
* original article sentiment/word
* generated article sentiment score
* generated article number of words
* generated article sentiment/word

For each temperature of 0.0, 0.5, and 1.0, chatGPT generated 5 different iterations of bullet points and articles. We then averaged the sentiment score of all 5 generated articles. In other words, for each original article, chatGPT generated 15 different bullet points and articles: 5 with a temperature setting of 0.0, 5 with a temperature setting of 0.5, and 5 with a temperature setting of 1.0.


### 2. Interpretation:

The interpretation phase had two components:
* General statistical analysis of the data
* Edge case study of cases where the original article sentimental score greatly differed from the generated article sentimental score.
