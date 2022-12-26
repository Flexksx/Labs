import json
from nltk.tokenize import word_tokenize

with open("resources\\tweets.json", "r", encoding='utf-8') as f:
    data = json.load(f)

tweets = []
for i in data:
    tweets.append(i)


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


def sortdict(somedict):
    a = sorted(somedict.items(), key=lambda x: x[1], reverse=True)
    ans = []
    for i in range(1, 11):
        ans.append(a[i])
    return ans


def elena():
    dicklist = []
    with open('resources\\AFINN-111.txt', 'r') as emotion:
        emotion = emotion.read()
    emotion = emotion.split()
    for i in range(0, len(emotion), 2):
        dicklist.append({emotion[i]: emotion[i + 1]})
    # json_object = json.dumps(dicklist, indent=4)
    # with open("resources\\emotions.json", "w") as new:
    #     new.write(json_object)
    return dicklist


def emotionval(message):
    values = elena()
    word_tokenize(message)
