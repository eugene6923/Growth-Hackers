from __future__ import division
import math, random, re
from collections import defaultdict, Counter
from bs4 import BeautifulSoup
import requests
import csv
with open('C:/temp/ddd.csv','r') as f :
    reader = csv.reader(f)
    a=list(reader)
documents=[]
for i in a :
    i = [x for x in i if x != '']
    documents.append(i)
print(documents
# topic의 개수
K = 4

# 조건부 확률 분포 정의를 위한 준비

# 1. 각 토픽이 각 문서에 할당되는 횟수
# counter로 구성된 list
# 각각의 counter는 각 문서를 의미함
document_topic_counts = [Counter() for _ in documents]

# 2. 각 단어가 각 토픽에 할당되는 횟수
# 각각의 counter는 각 토픽을 의미함
topic_word_counts = [Counter() for _ in range(K)]

# 3. 각 토픽에 할당되는 총 단어 수
# 각각의 숫자는 각 토픽을 의미함
topic_counts = [0 for _ in range(K)]

# 4. 각 문서에 포함되는 총 단어의 수
# 각각의 숫자는 각 문서를 의미함
document_lengths = [len(d) for d in documents]

# 5. 단어 종류의 수
distinct_words = set(word for document in documents for word in document)
W = len(distinct_words)

# 6. 총 문서의 수
D = len(documents)

# 각 단어를 임의의 토픽에 배정하고, 필요한 수치를 계산하기
random.seed(0)
document_topics = [[random.randrange(K) for word in document]
                   for document in documents]

for d in range(D):
    for word, topic in zip(documents[d], document_topics[d]):
        document_topic_counts[d][topic] += 1
        topic_word_counts[topic][word] += 1
        topic_counts[topic] += 1


# 각 토픽이 모든 문서에 대해 0 이상의 확률을 가지도록 smoothing하기
def p_topic_given_document(topic, d, alpha=0.1):
    """the fraction of words in document _d_
     that are assigned to _topic_ (plus some smoothing)"""

    return ((document_topic_counts[d][topic] + alpha) /
            (document_lengths[d] + K * alpha))


def p_word_given_topic(word, topic, beta=0.1):
    """the fraction of words assigned to _topic_
    that equal _word_ (plus some smoothing)"""

    return ((topic_word_counts[topic][word] + beta) /
            (topic_counts[topic] + W * beta))


# 랜덤으로 생성된 weight로부터 인덱스를 생성함
def sample_from(weights):
    total = sum(weights)
    rnd = total * random.random()  # uniform between 0 and total
    for i, w in enumerate(weights):
        rnd -= w  # return the smallest i such that
        if rnd <= 0: return i  # sum(weights[:(i+1)]) >= rnd


# 토픽을 업데이트 하기 위한 weight 생성하기
def topic_weight(d, word, k):
    """문서와 문서의 단어가 주어지면, K번째 토픽의 weight를 반환"""
    return p_word_given_topic(word, k) * p_topic_given_document(k, d)


def choose_new_topic(d, word):
    return sample_from([topic_weight(d, word, k)
                        for k in range(K)])


# 조건부 확률 분포를 이용하여 (토픽-단어), (문서-토픽)에 대한 깁스 샘플링 실행하기
for iter in range(1000):
    for d in range(D):
        for i, (word, topic) in enumerate(zip(documents[d],
                                              document_topics[d])):
            # remove this word / topic from the counts
            # so that it doesn't influence the weights
            document_topic_counts[d][topic] -= 1
            topic_word_counts[topic][word] -= 1
            topic_counts[topic] -= 1
            document_lengths[d] -= 1

            # choose a new topic based on the weights
            new_topic = choose_new_topic(d, word)
            document_topics[d][i] = new_topic

            # and now add it back to the counts
            document_topic_counts[d][new_topic] += 1
            topic_word_counts[new_topic][word] += 1
            topic_counts[new_topic] += 1
            document_lengths[d] += 1

# 각 토픽에 가장 영향력이 높은 (weight)값이 큰 단어 탐색
for k, word_counts in enumerate(topic_word_counts):
    for word, count in word_counts.most_common():
        if count > 0: print(k, word, count)

topic_names = ["topic1",
               "topic2",
               "topic3",
               "topic4"]

for document, topic_counts in zip(documents, document_topic_counts):
    print(document)
    for topic, count in topic_counts.most_common():
        if count > 0:
            print(topic_names[topic], count)
