import pandas as pd
import matplotlib.pyplot as plt

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

# Plot normalized data on a bar chart
fig = plt.figure(figsize=(12, 6)) # Resize FIgure
plt.bar(df.index, df['retweet_count_norm'], label='retweet_count_norm')
plt.bar(df.index, df['reply_count_norm'], bottom=df['retweet_count_norm'], label='reply_count_norm')
plt.bar(df.index, df['like_count_norm'], bottom=df['reply_count_norm']+df['retweet_count_norm'], label='like_count_norm')
plt.bar(df.index, df['impression_count_norm'], bottom=df['like_count_norm']+df['reply_count_norm']+df['retweet_count_norm'], label='impression_count_norm')
plt.legend()
plt.show()