import pandas as pd

# reading the csv into a dataframe
df = pd.read_csv("./Assignments/assignment2/tweetsSample.csv")

# Removing blank columns 
df = df.dropna(subset=['time'])

# Removes duplicate values 
def isDup(tweet1, tweet2, threshold = 0.7):

    # Spliting the tweets into words 
    tweet_words1 = set(tweet1.lower().split())
    tweet_words2 = set(tweet2.lower().split())

    # Determining which tweet has more words 
    if len(tweet_words1) > len(tweet_words2):
        words_max = len(tweet_words1)
    else:
        words_max = len(tweet_words2)

    # Set of matching words 
    matching_words = tweet_words1 & tweet_words2

    # Determines if the fraction of matched words is over the threshold
    if len(matching_words)/words_max >threshold:
        return True
    else:
        return False

#Comparing the text in each row 
for i in range(0, len(df)-1):
    val1 = df.loc[i, 'text']
    val2 = df.loc[i + 1, 'text']
    df.loc[i, 'isDup'] = float(isDup(val1, val2))

# Message
print(f"There are {df['isDup'].sum()} duplicates with a similarity of 70% that are removed.")

# Removing true rows
df = df[df['isDup'] != True]

# Removing time and id column
df = df.drop('time', axis = 1)
df = df.drop('id', axis = 1)

# Back to csv
df.to_csv('./Assignments/assignment2/processedData.csv', index=False)
