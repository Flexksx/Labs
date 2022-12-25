import json

with open("resources\\tweets.json", "r", encoding='utf-8') as f:
    data = json.load(f)

tweets = []
for i in data:
    tweets.append(i)


def gethashtags(tuitz):
    for i in tuitz:
        print(i['text'])
    hashtags = {}
    for i in tuitz:
        text = i['text'].split()
        for j in text:
            if j[0] == '#' and j not in hashtags:
                hashtags.update({j: 0})
            elif j[0] == '#':
                hashtags[j] += 1
    return hashtags


def getmostpop(somedict):
    return sorted(somedict.items(), key=lambda x:x[1])

print(getmostpop(gethashtags(tweets)))
