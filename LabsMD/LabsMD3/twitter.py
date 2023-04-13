import json
import nltk
from nltk import TweetTokenizer

with open("resources/tweets.json", "r", encoding='utf-8') as f:
    data = json.load(f)

tweets = []
for i in data:
    tweets.append(i)

tt = TweetTokenizer()


def gethashtags(tuitz):
    hashtags = {}
    for i in tuitz:
        text = i['text'].split()
        for j in text:
            if j[0] == '#' and j not in hashtags:
                hashtags.update({j: 1})
            elif j[0] == '#':
                hashtags[j] += 1
        for j in hashtags:
            for q in text:
                if j in q and j != q:
                    hashtags[j] += 1
    return hashtags


def sortdict(somedict, rev):
    a = sorted(somedict.items(), key=lambda x: x[1], reverse=rev)
    ans = []
    for i in range(1, 11):
        ans.append(a[i])
    return ans


def emotions():
    dicklist = {}
    with open("resources/AFINN-111.txt", "r", encoding="utf-8") as AFINNdict:
        for line in AFINNdict:
            words = nltk.word_tokenize(line)
            nr = words[len(words) - 1]
            strn = ""
            for x in range(len(words) - 1):
                strn += words[x]
            dicklist[strn] = nr
    return dicklist


def emotionval(tweets):
    values = emotions()
    ans = {}
    for x in tweets:
        ans.update({x['text']: 0})
    for x in ans:
        tweet = tt.tokenize(x)
        for word in tweet:
            for val in values:
                if word == val:
                    ans[x] += int(values[val])
    return ans


def EmotionalValuesOut(valued):
    print("Top Most negative tweets")
    ans = sortdict(valued, False)
    for x in ans:
        print(x)
    print("Top Most Positive tweets")
    ans = sortdict(valued, True)
    for x in ans:
        print(x)


def storeintxt(tweets):
    ans = emotionval(tweets)
    anslist=[]
    for x in ans:
        print(x,ans[x])
    with open("evaluated.json", 'w', encoding='utf-8') as f:
        json.dump(ans,f)


EmotionalValuesOut(emotionval(tweets))
