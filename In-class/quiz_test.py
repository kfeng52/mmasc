

def happywords(tweet, happy_list):
    tweet_words = tweet.split()
    matches = 0
    words = 0

    for word in tweet_words:
        words += 1
        if word in happy_list:
            matches += 1

    return matches, words

def identifyHappiness(userRng, tweetRng, happy_list):
    list_user = {}
    list_user_happiness = {}


    for tweet in range(0, len(tweetRng)):
        user = userRng[tweet] 
        tweet_content = tweetRng[tweet] 
        if user in list_user:
            list_user[user].append(tweet_content)
        else:
            list_user[user] = [tweet_content]

    for user in list_user:
        user_happy_count = 0
        user_words = 0

        for tweet in list_user[user]:
            happy_words, tweet_words = happywords(tweet, happy_list)
            user_happy_count += happy_words
            user_words += tweet_words

        #print(f"{user}'s total number of words is {user_words}")
        #print(f"{user}'s total number of happy words is {user_happy_count}")

        if user_happy_count/user_words >= 0.3:
            list_user_happiness[user] = 'happy'
        else:
            print(user)
            list_user_happiness[user] = 'unhappy'
    
    print(list_user_happiness)
        

            
happy_words = ['happy']

x = ['bob', 'bob', 'joe', 'asied']
y = ['happy sappy nappy', 'happy happy happy', 'sad dads sad', 'i wanna kill myself']

identifyHappiness(x,y,happy_words)