import json
import matplotlib.pyplot as plt
import nltk
from nltk import TweetTokenizer

tt = TweetTokenizer()
special_chars = "1234567890#@.=?\",”$%^&’*(…[]):!><"
likes_per_id = {}
retweets_per_id = {}
filter_words = ["sure"]
words_tweet_tokenizer = []
words_set = []
word_count_not_case_sensitive = {}
words_per_tweet = {}
special_words = []
hashtags = []


def GetWords():
    word_count_dict = {}
    with open("C:\\Users\\Cristi\\Documents\\GitHub\\Labs\\Labs3\\LabsMD3\\resources\\tweets.json", "r",
              encoding="utf-8") as tweetJson:
        tweetJsonData = json.load(tweetJson)
        for tweet in tweetJsonData:
            tempWords = tt.tokenize(tweet["text"])
            words_per_tweet[tweet["id"]] = tempWords
            for word in tempWords:
                if not any(c in special_chars for c in word) and len(word) > 1:
                    words_tweet_tokenizer.append(word)
                    if word not in word_count_not_case_sensitive:
                        word_count_not_case_sensitive[word] = 1
                    else:
                        word_count_not_case_sensitive[word] += 1
                    if word not in word_count_dict and word.lower() not in word_count_dict:
                        word_count_dict[word.lower()] = 1
                    else:
                        word_count_dict[word.lower()] += 1
                    if word[0] == '#':
                        hashtags.append(word)
                    if word not in words_set:
                        words_set.append(word)
                else:
                    if len(word) > 1:
                        special_words.append(word)
    return dict(sorted(word_count_dict.items(), key=lambda item: item[1], reverse=True))


def TopWords():
    words = GetWords()
    x = 1
    for i in words:
        if x <= 10:
            print(i, " ", words[i])
        x += 1


def WordPerMonth():
    month_and_noun = {'2020-10': 0, '2020-11': 0, '2020-12': 0, '2022-01': 0, '2022-02': 0, '2022-03': 0, '2022-11': 0}
    word = input("Write a word")
    with open('C:\\Users\\Cristi\\Documents\\GitHub\\Labs\\Labs3\\LabsMD3\\resources\\tweets.json', 'r',
              encoding='utf-8') as tweet_json:
        tweet_data = json.load(tweet_json)
        for i in range(len(tweet_data)):
            temp_msg = nltk.word_tokenize(tweet_data[i]["text"])
            temp_date = nltk.word_tokenize(tweet_data[i]["created_at"])
            for x in temp_msg:
                if x == word or x.lower() == word:
                    month_and_noun[temp_date[0][:7]] += 1
    x = list(month_and_noun.keys())
    y = list(month_and_noun.values())
    plt.bar(x, y, color='maroon', width=0.7)
    plt.show()


def CountNouns():
    words = GetWords()
    nouns_counted = {}
    for i in words:
        ans = nltk.pos_tag([i])[0][1]
        if ans == 'NN' or ans == 'NNS' or ans == 'NNPS' or ans == 'NNP':
            if i not in filter_words and not any(c in ["\'"] for c in i):
                nouns_counted[i] = words[i]
    nouns_counted = dict(sorted(nouns_counted.items(), key=lambda item: item[1], reverse=True))

    def PopularityNouns():
        with open('C:\\Users\\Cristi\\Documents\\GitHub\\Labs\\Labs3\\LabsMD3\\resources\\tweets.json', 'r',
                  encoding='utf-8') as tweet_json:
            tweet_data = json.load(tweet_json)
            for tweet in tweet_data:
                likes_per_id[tweet["id"]] = tweet["likes"]
                retweets_per_id[tweet["id"]] = tweet["retweets"]
        popularity_nouns = {}
        word_count_dict = GetWords()
        for noun in nouns_counted:
            normLikes = 0
            normRetweets = 0
            for id in words_per_tweet:
                if noun in words_per_tweet[id]:
                    normLikes += likes_per_id[id]
                    normRetweets += retweets_per_id[id]
            popularity_nouns[noun] = word_count_dict[noun] * (1.4 * normRetweets) * (1.2 * normLikes)
        return dict(sorted(popularity_nouns.items(), key=lambda item: item[1], reverse=True))

    def ProperNouns():
        # Counts proper nouns
        proper_nouns_counted = {}
        for i in word_count_not_case_sensitive:
            ans = nltk.pos_tag([i])[0][1]
            if ans == 'NN' or ans == 'NNS' or ans == 'NNPS' or ans == 'NNP':
                if i not in filter_words and not any(c in ["\'"] for c in i) and i[0].isupper():
                    proper_nouns_counted[i] = word_count_not_case_sensitive[i]
        return dict(sorted(proper_nouns_counted.items(), key=lambda item: item[1], reverse=True))

    def OutPropNouns():
        proper_nouns_counted = ProperNouns()
        print("===================")
        print("Top 10 proper nouns")
        print("===================")
        x = 1
        for i in proper_nouns_counted:
            if x <= 10:
                print(i, " ", proper_nouns_counted[i])
            x += 1

    def OutPopNouns():
        # Outputs popularity nouns
        popularity_nouns = PopularityNouns()
        print("==========================")
        print("Top 10 nouns by popularity")
        print("==========================")
        x = 1
        for i in popularity_nouns:
            if x <= 10:
                print(i, " ", popularity_nouns[i])
            x += 1

    def OutNouns():
        print("============")
        print("Top 10 nouns")
        print("============")
        x = 1
        for i in nouns_counted:
            if x <= 10:
                print(i, " ", nouns_counted[i])
            x += 1

    OutNouns()
    OutPopNouns()
    OutPropNouns()


def Suggestion():
    def GetSugg():
        # Suggestion stuff
        word_count_dict = GetWords()
        word_sliced_count = {}
        word = input("Write word for suggestion")
        for x in word_count_dict:
            if x not in word_sliced_count:
                word_sliced_count[x] = 0
        for x in word_count_dict:
            if word == x[:len(word)] and word != x:
                word_sliced_count[x] += word_count_dict[x]
        return dict(sorted(word_sliced_count.items(), key=lambda item: item[1], reverse=True))

    def Out():
        words = GetSugg()
        x = 1
        for i in words:
            if x <= 10:
                print(i, " ", words[i])
            x += 1

    GetSugg()
    Out()


def SuggOcc():
    def GetOcc():
        # Suggestion occurrences stuff
        word = input("Write word for suggestion")
        words_suggestion_counted = {}
        for id in words_per_tweet:
            for i in range(len(words_per_tweet[id]) - 2):
                if words_per_tweet[id][i] == word:
                    if words_per_tweet[id][i + 1] not in words_suggestion_counted and len(
                            words_per_tweet[id][i + 1]) > 1:
                        words_suggestion_counted[words_per_tweet[id][i + 1]] = 1
                    elif len(words_per_tweet[id][i + 1]) > 1:
                        words_suggestion_counted[words_per_tweet[id][i + 1]] += 1
        return dict(sorted(words_suggestion_counted.items(), key=lambda item: item[1], reverse=True))

    def Out():
        words = GetOcc()
        print("Top suggestion occurrences")
        x = 1
        for i in words:
            if x <= 5:
                print(i, " ", words[i])
            x += 1

    GetOcc()
    Out()

# TopWords()
# CountNouns()
# Suggestion()
# SuggOcc()
# WordPerMonth()
