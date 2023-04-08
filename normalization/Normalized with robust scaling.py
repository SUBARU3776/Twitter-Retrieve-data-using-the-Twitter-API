import pandas as pd
from sklearn.preprocessing import RobustScaler

# Load CSV file
df = pd.read_csv("C:/hogehoge.csv")

# Robust scaling for retweet_count, reply_count, like_count, and impression_count
scaler = RobustScaler()
df[['retweet_count_norm', 'reply_count_norm', 'like_count_norm', 'impression_count_norm']] = scaler.fit_transform(df[['retweet_count', 'reply_count', 'like_count', 'impression_count']])

# Output scaled data
print(df[['retweet_count_norm', 'reply_count_norm', 'like_count_norm', 'impression_count_norm']])

# Save data as a CSV file
df.to_csv("C:hogehoge.robust scaling.csv", index=False)
