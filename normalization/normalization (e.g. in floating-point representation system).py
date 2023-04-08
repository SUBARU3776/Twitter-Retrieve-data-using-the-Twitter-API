import pandas as pd

# Load CSV file
df = pd.read_csv("C:/hogehoge.csv")

# Find the minimum and maximum values of retweet_count, reply_count, like_count, and impression_count
min_retweet_count = df['retweet_count'].min()
max_retweet_count = df['retweet_count'].max()
min_reply_count = df['reply_count'].min()
max_reply_count = df['reply_count'].max()
min_like_count = df['like_count'].min()
max_like_count = df['like_count'].max()
min_impression_count = df['impression_count'].min()
max_impression_count = df['impression_count'].max()

# Normalize retweet_count, reply_count, like_count, and impression_count
df['retweet_count_norm'] = (df['retweet_count'] - min_retweet_count) / (max_retweet_count - min_retweet_count)
df['reply_count_norm'] = (df['reply_count'] - min_reply_count) / (max_reply_count - min_reply_count)
df['like_count_norm'] = (df['like_count'] - min_like_count) / (max_like_count - min_like_count)
df['impression_count_norm'] = (df['impression_count'] - min_impression_count) / (max_impression_count - min_impression_count)

# Output normalized data
print(df[['retweet_count_norm', 'reply_count_norm', 'like_count_norm', 'impression_count_norm']])

# Save data as a CSV file
df.to_csv("C:/hogehoge.normalization.csv", index=False)
