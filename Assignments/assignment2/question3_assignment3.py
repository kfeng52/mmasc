import pandas as pd

df = pd.read_csv("./Assignments/assignment2/processedKeywordData.csv")

# CountIfs Function
def myCountIfs(range1, criteria1, range2, criteria2):
    condition1 = range1 == criteria1
    condition2 = range2 == criteria2
    count = (condition1 & condition2).sum()
    return count

# Average If Function 
def myAverageIf(range_to_average, range_for_criteria, criteria):
    filtered_values = range_to_average[range_for_criteria == criteria]
    average = filtered_values.mean()
    return average

# Max element
def findMaxElement(rangeName, rangeValues):
    max_index = rangeValues.idxmax()
    return rangeName[max_index]

# Topics
topics = df['topic'].unique().tolist()
topics.sort()

# Groups
groups = df['group'].unique().tolist()
groups.sort()

# Topics dictionary with groups
tg = {}
for i in topics:
    tg[i] = [df.loc[df['topic'] == i, 'group'].iloc[0]]

# Sorting topics and groups by groups 
tg_sorted = dict(sorted(tg.items(), key=lambda item: item[1]))

# Groups dictionary
gr = {}
for i in groups:
    gr[i] = []

# Task A
for i in topics:
    tg_sorted[i].append(round(myAverageIf(df['sentimentValue'], df['topic'], i), 4))

# Task B
for i in groups:
    gr[i].append(round(myAverageIf(df['sentimentValue'], df['group'], i),4))

# Task C
for i in topics:
    tg_sorted[i].append(myCountIfs(df['topic'], i, df['sentiment'], "Positive"))
    tg_sorted[i].append(myCountIfs(df['topic'], i, df['sentiment'], "Neutral"))
    tg_sorted[i].append(myCountIfs(df['topic'], i, df['sentiment'], "Negative"))

# Task D
for i in groups:
    gr[i].append(myCountIfs(df['group'], i, df['sentiment'], "Positive"))
    gr[i].append(myCountIfs(df['group'], i, df['sentiment'], "Neutral"))
    gr[i].append(myCountIfs(df['group'], i, df['sentiment'], "Negative"))

# Task E

value_counts = df['sentiment'].value_counts()
task_e = [value_counts.iloc[1], value_counts.iloc[0], value_counts.iloc[2]]


# Task F
topic_high_sent = findMaxElement(df['topic'], df['sentimentValue'])

# Task G
group_high_sent = findMaxElement(df['group'], df['sentimentValue'])

# changing the dictionary to a df 
formatted_dict = {key: [key] + values for key, values in tg_sorted.items()}
df1 = pd.DataFrame.from_dict(tg_sorted, orient='index')
df1 = df1.reset_index()

formatted_dict = {key: [key] + values for key, values in gr.items()}
df2 = pd.DataFrame.from_dict(gr, orient='index')
df2 = df2.reset_index()

# file path
csv_file = 'analyzedData.csv'

# Write DataFrame 1 
df1.to_csv(csv_file, index=False)

# Add a blank row b
with open(csv_file, mode='a') as f:
    f.write('\n')

# Write DataFrame 2 
df2.to_csv(csv_file, mode='a', header=False, index=False)

# Add another blank row 
with open(csv_file, mode='a') as f:
    f.write('\n')

# Write the list and variables as additional content 
with open(csv_file, mode='a') as f:
    f.write(f"{task_e[0]},{task_e[1]},{task_e[2]}\n")
    f.write(f"{topic_high_sent}\n{group_high_sent}\n")




