import pandas as pd

df = pd.read_csv("../../fake/BuzzFeed_fake_news_grouped_temp_data_diff.csv")

left_wing_sources = [
    'http://www.addictinginfo.org',
    'http://winningdemocrats.com',
    'http://occupydemocrats.com',
    'http://addictinginfo.org',
     'http://www.ifyouonlynews.com',
     'http://author.groopspeak.com'
]

right_wing_sources = [
    'http://eaglerising.com',
    'http://allenwestrepublic.com',
    'http://100percentfedup.com',
    'http://rightwingnews.com',
    'http://usherald.com',
    'http://theblacksphere.net',
    'http://freedomdaily.com',
    'http://www.yesimright.com',
    'http://clashdaily.com',
    'http://www.chicksontheright.com',
    'http://www.thepoliticalinsider.com',
    'http://conservativetribune.com',
    'https://ihavethetruth.com'
]

left_leaning_data = df[df['source'].isin(left_wing_sources)]
right_leaning_data = df[df['source'].isin(right_wing_sources)]

left_leaning_data.to_csv("leftWingFakeaa.csv", index=False)
right_leaning_data.to_csv("rightWingFakeaa.csv", index=False)