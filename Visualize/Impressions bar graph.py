import pandas as pd
import matplotlib.pyplot as plt

# Import data from CSV files
df = pd.read_csv("D:\hogehoge.csv")

# Convert created_at column to date type
df.loc[:, 'created_at'] = pd.to_datetime(df['created_at']).dt.date

# Filtering time period
start_date = pd.to_datetime('2023-02-01').date()
end_date = pd.to_datetime('2023-03-01').date()
counts_df = df.loc[(df['created_at'] >= start_date) & (df['created_at'] <= end_date), ['created_at', 'retweet_count', 'quote_count', 'reply_count', 'like_count', 'impression_count']].copy()
# start_date = pd.to_datetime('2023-02-01').date()
# counts_df = df.loc[df['created_at'] >= start_date, ['created_at', 'retweet_count', 'quote_count', 'reply_count', 'like_count', 'impression_count']].copy()

# Set created_at column as index
counts_df.set_index('created_at', inplace=True)

# Create functions for plotting graphs
def plot_graph(ax, x, y, label):
    ax.bar(x, y)
    ax.text(0.5, 0.9, label, ha='center', transform=ax.transAxes)

# Create area to display graphs
fig, axs = plt.subplots(nrows=5, figsize=(16, 20))

# Draw a graph for each column
plot_graph(axs[0], counts_df.index, counts_df['retweet_count'], 'retweet_count')
plot_graph(axs[1], counts_df.index, counts_df['quote_count'], 'quote_count')
plot_graph(axs[2], counts_df.index, counts_df['reply_count'], 'reply_count')
plot_graph(axs[3], counts_df.index, counts_df['like_count'], 'like_count')
plot_graph(axs[4], counts_df.index, counts_df['impression_count'], 'impression_count')

# Set x-axis and y-axis labels
fig.text(0.5, 0.04, 'Date', ha='center')
fig.text(0.04, 0.5, 'Count', va='center', rotation='vertical')

# Display Graphs
plt.show()
