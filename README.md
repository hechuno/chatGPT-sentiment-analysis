# Sentiment Analysis of Content Created by chatGPT

Under the supervision of Professor Raphaël Khoury, this is my final project to obtain my bachelor's in computer science from the University of Québec in Outaouais.

## Objective

ChatGPT is writing more content. Ideally, chatGPT would use unbiased and factual language. This research seeks to find if the content created by chatGPT is positive, neutral, or negative. In particular, it seeks to find if chatGPT is biased towards certain subjects and if/how much the temperature parameter affects the language used by chatGPT. We used the chatGPT 4o-mini model and the chatGPT API to generate the data.

## Discussion

This research examined ChatGPT's behavior in content generation, specifically the generation of news articles based on instructions and data provided in the form of bullet points. While no definitive conclusion can be drawn that ChatGPT generates content with a political bias, some observations warrant attention:

### Key Observations

1. Language Tone:

  * ChatGPT tends to use more positive language with left-leaning articles. However, this does not necessarily imply a bias toward the left. It might reflect the nature of the original left-leaning articles used as input data, which often employ particularly negative language to describe the right and figures like Donald Trump. In contrast, ChatGPT employs more neutral or modest language when describing the right.

2. Data Limitations:

  * The dataset used in this study was insufficient to draw conclusions, particularly due to the limited number of left-leaning articles.

  * The starting parameters were not ideal; the sentiment scores (a measure of positivity or negativity) of the original articles were not balanced between the left-leaning and right-leaning articles, it would be better to have similar sentimental scores between the left-leaning and right-leaning articles.

  * The size and subject matter of the original articles varied significantly.

3. Sentiment Distribution:

  * Both the original and ChatGPT-generated articles’ sentiment scores followed a normal distribution. This suggests that the events or themes covered in the articles evoked a balanced range of emotions, from negative to positive, with the majority being neutral or slightly negative for the dataset examined.

4. Positivity Bias:

  * ChatGPT tends to use positive language, potentially for several reasons:

    * It frequently adds positive adjectives to describe statistics.

    * It might employ different word choices depending on whether it’s writing in the first or third person.

5. Handling Sarcasm:

  * ChatGPT does not replicate sarcasm from the original articles. Instead, it explicitly explains the underlying ideas and emotions.

  * In edge cases, sarcasm, which often uses positive words in a negative context, resulted in ChatGPT’s language being perceived as more negative by sentiment analysis algorithms like Afinn, which cannot detect sarcasm effectively. For example, the expression "good Molotov cocktail" has a sentimental score of +2.0, because of the word "good". Afinn cannot detect that it is used in a sarcastic, negative manner.

6. Objectivity Correlation:

  * According to the Spearman test, ChatGPT’s generated articles tend to mirror the sentiment trend of the original articles. If the original articles use positive language, ChatGPT’s output is also likely to be positive.

7. Temperature Parameter:

  * The temperature parameter (degree of creative freedom in ChatGPT’s API) has a negligible effect on the sentiment scores of generated articles.

  * Higher temperature settings result in longer outputs, although ChatGPT struggles to generate more than 1,000 words in a single prompt.

### Recommendations for Future Research

1. Weighted Sentiment Calculation:

  * Revise the calculation of average sentiment scores by assigning more weight to longer articles. This adjustment will ensure that articles with more words contribute proportionally more to the analysis, reducing the influence of edge cases.

2. Improved Dataset:

  * Use a larger, more balanced dataset with equal sentiment scores across left-leaning and right-leaning articles to minimize variability.

3. Expanded Parameters:

  * Examine the impact of temperature settings on content size, structure, and sentiment with more controlled experiments.

### Conclusion

This study builds on previous research into ChatGPT’s objectivity and potential biases, introducing a new method that combines content generation with sentiment analysis using tools like Afinn and statistical interpretation. Future studies could explore these findings with improved methodologies, datasets, and a more narrow focus.

### Additional Information

You are encouraged to review the data and generated articles for yourself. If you have any questions or require clarification, please don’t hesitate to reach out.

**Please reference the report for details. It is in French.**
