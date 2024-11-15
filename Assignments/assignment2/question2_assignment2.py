import pandas as pd

# reading the csv into a dataframe
df_keywords = pd.read_csv("./Assignments/assignment2/keywords.csv")
df_text = pd.read_csv("./Assignments/assignment2/processedData.csv", header=None)

# Storing the key words in lists 
neg_words = df_keywords['NegativeWords'].tolist()
pos_words = df_keywords['PositiveWords'].tolist()

# Determine Sentiment Category
def sentimentCategory(sentVal):
    if sentVal > 0:
        return 'Positive'
    elif sentVal == 0: 
        return 'Neutral'
    elif sentVal < 0:
        return 'Negative'

# Calculate the sentiment of each score 
for i in range(0, len(df_text)):
    score = 0 
    text = df_text.loc[i, 0]
    text = text.lower().split()

    # Determining the number of positive and negative words 
    num_positive_words = len([word for word in text if word in pos_words])
    num_negative_words = len([word for word in text if word in neg_words])

    # Calculating the score 
    score = num_positive_words*10 - num_negative_words*10

    # Storing the sentiment value in the df 
    df_text.loc[i, 5] = sentimentCategory(score)

# Back to csv
df_text.to_csv('./Assignments/assignment2/processedKeywordData.csv', index=False, header=None)



