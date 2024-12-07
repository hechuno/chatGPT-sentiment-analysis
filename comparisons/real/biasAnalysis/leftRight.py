import pandas as pd

df = pd.read_csv("BuzzFeed_real_news_grouped_temp_data_diff.csv")

left_wing_sources = [
    'http://www.addictinginfo.org',
    'http://winningdemocrats.com',
    'http://occupydemocrats.com',
    'http://addictinginfo.org',
     'http://www.ifyouonlynews.com'
]

right_wing_sources = [
    'http://eaglerising.com',
    'http://rightwingnews.com',
    'http://freedomdaily.com'
]

neutral_sources = [
    'http://abcn.ws',
    'http://cnn.it',
    'http://politi.co',
    'https://www.washingtonpost.com'
    
]

left_leaning_data = df[df['source'].isin(left_wing_sources)]
right_leaning_data = df[df['source'].isin(right_wing_sources)]
neutral_data = df[df['source'].isin(neutral_sources)]

left_leaning_data.to_csv("leftWingReal.csv", index=False)
right_leaning_data.to_csv("rightWingReal.csv", index=False)
neutral_data.to_csv("neutralReal.csv", index=False)