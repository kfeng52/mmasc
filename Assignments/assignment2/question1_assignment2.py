import pandas as pd

# reading the csv into a dataframe
df = pd.read_csv("./Assignments/assignment2/tweetsSample.csv", header=None)

# Removing blank columns 
df = df.dropna(subset=[0])

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

# Removing empty column: data cleaning 
df = df.drop(5, axis = 1)

#Comparing the text in each row 
for i in range(0, len(df)-1):
    val1 = df.loc[i, 1]
    val2 = df.loc[i + 1, 1]
    result = isDup(val1, val2)  
    df.loc[i, 5] = float(result)

# Removing true rows
df = df[df[5] != True]

# Message
print(f"There are {df[5].sum()} duplicates with a similarity of 70% that are removed.")

# Removing time column (0)
df = df.drop(0, axis = 1)

# Back to csv
df.to_csv('./Assignments/assignment2/processedData.csv')
