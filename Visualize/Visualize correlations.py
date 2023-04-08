import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Import CSV files
df = pd.read_csv("D:\hogehoge.csv")

# Calculate the correlation between 'retweet_count', 'reply_count', 'like_count' and 'impression_count
correlation = df[['retweet_count', 'reply_count', 'like_count', 'impression_count']].corr()

# Display correlation matrix
print(correlation)

# Draw a heat map of the correlation matrix
sns.heatmap(correlation, annot=True, cmap='coolwarm', linewidths=0.5)
plt.show()