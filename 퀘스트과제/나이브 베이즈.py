#필요한 것 불러오기
from numpy import *

# 자료 넣어주기
def loadDataSet():
    postingList = [['I', 'got', 'free', 'two', 'movie', 'ticket', 'from', 'your', 'boy', 'friend'],

                   ['free', 'coupon', 'from', 'xx.com'],

                   ['watch', 'free', 'new', 'movie', 'from', 'freemovie.com'],

                   ['best', 'deal', 'promo', 'code', 'here'],

                   ['there', 'will', 'be', 'free', 'pizza', 'during', 'the', 'meeting'],

                   ['scheduled', 'meeting', 'tomorrow'],

                   ['can', 'we', 'have', 'lunch', 'today'],

                   ['I', 'miss', 'you'],

                   ['thanks', 'my', 'friend'],

                   ['it', 'was', 'good', 'to', 'see', 'you', 'today'],

                   ['free', 'coupon', 'last', 'deal'],

                   ['free', 'massage', 'coupon'],

                   ['I', 'sent', 'the', 'coupon', 'you', 'asked', 'it', 'is', 'not', 'free'],

                   ['coupon', 'promo', 'code', 'here']]

    classVec = [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1]  # 1은 스팸 그리고 0은 스팸으로 지정해주기
#postingList는 안에 글자가 들어가있고 classVec은 각 line마다 spam인지 아닌지가 들어있다.
    return postingList, classVec

# 글자넣고 합쳐주는 함수 정의해주기
def createVocabList(dataSet):
    vocabSet = set([])  # 공간을 만들어준다.

    for document in dataSet:
        vocabSet = vocabSet | set(document)  # 두개의 세트를 합쳐준다

    return list(vocabSet)

def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0] * len(vocabList)

    for word in inputSet:

        if word in vocabList:

            returnVec[vocabList.index(word)] = 1

        else:
            print
        "the word: %s is not in my Vocabulary!" % word

    return returnVec


def trainNB00(trainMatrix, trainCategory):
    numTrainDocs = len(trainMatrix) #길이지정

    numWords = len(trainMatrix[0])

    pSpam = sum(trainCategory) / float(numTrainDocs) #스팸일 확률 구하기

    p0Num = zeros(numWords);
    p1Num = zeros(numWords)

    p0Denom = 0.0;
    p1Denom = 0.0

    for i in range(numTrainDocs):

        if trainCategory[i] == 1:

            p1Num += trainMatrix[i]#단어포함 스팸갯수

            p1Denom += sum(trainMatrix[i])#전체 스팸갯수

        else:

            p0Num += trainMatrix[i]#단어포함 스팸아닌것의

            p0Denom += sum(trainMatrix[i])#전체 스팸아닌것의

    p1Vect = p1Num / p1Denom

    p0Vect = p0Num / p0Denom

    return p0Vect, p1Vect, pSpam


def trainNB0(trainMatrix, trainCategory):
    numTrainDocs = len(trainMatrix) #길이지정

    numWords = len(trainMatrix[0])

    pSpam = sum(trainCategory) / float(numTrainDocs) #스팸일 확률구하기

    p0Num = ones(numWords);
    p1Num = ones(numWords)

    p0Denom = 2.0;
    p1Denom = 2.0

    for i in range(numTrainDocs):

        if trainCategory[i] == 1:

            p1Num += trainMatrix[i]#스팸이었던 것의 수를 구하기

            p1Denom += sum(trainMatrix[i])#스팸 총 갯수 구하기

        else:

            p0Num += trainMatrix[i]

            p0Denom += sum(trainMatrix[i])

    p1Vect = log(p1Num / p1Denom)#스팸아닌것에서 스팸이었던것의 확률를 로그안에 넣기

    p0Vect = log(p0Num / p0Denom)

    return p0Vect, p1Vect, pSpam


def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    #로그에 넣어서 원래는 각 조건부 확률을 곱해주는 것을 더해주는 것으로 바꿔준다.
    p1 = sum(vec2Classify * p1Vec) + log(pClass1)  # element-wise mult

    p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)

    if p1 > p0:

        return 1

    else:

        return 0


def bagOfWords2VecMN(vocabList, inputSet):
    returnVec = [0] * len(vocabList)

    for word in inputSet:

        if word in vocabList:
            returnVec[vocabList.index(word)] += 1

    return returnVec


def testingNB():
    listOPosts, listClasses = loadDataSet()

    myVocabList = createVocabList(listOPosts)

    trainMat = []

    for postinDoc in listOPosts:
        trainMat.append(setOfWords2Vec(myVocabList, postinDoc))

    # print(str(trainMat))

    p0V, p1V, pSpam = trainNB0(array(trainMat), array(listClasses))

    testEntry = ['free', 'pizza', 'coupon']

    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))

#1일대는 스팸으로 분류하고 다른 것일때는 스팸이 아닌 것으로 분류하기
    if classifyNB(thisDoc, p0V, p1V, pSpam) == 1:

        print
        testEntry, 'classified this is a spam'

    else:

        print
        testEntry, 'classified this is not a spam'

    testEntry = ['I', 'will', 'miss', 'free', 'pizza']

    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))

    if classifyNB(thisDoc, p0V, p1V, pSpam) == 1:

        print
        testEntry, 'classified this is a spam'

    else:

        print
        testEntry, 'classified this is not a spam'


def textParse(bigString):  # input is big string, #output is word list

    import re

    listOfTokens = re.split(r'\W*', bigString)

    return [tok.lower() for tok in listOfTokens if len(tok) > 2]


def spamTest(): #스팸트레인의 정확도 측정하기
    docList = [];
    classList = [];
    fullText = []

    for i in range(1, 26):
        wordList = textParse(open('email/spam/%d.txt' % i).read())

        docList.append(wordList)

        fullText.extend(wordList)

        classList.append(1)

        wordList = textParse(open('email/ham/%d.txt' % i).read())

        docList.append(wordList)

        fullText.extend(wordList)

        classList.append(0)

    vocabList = createVocabList(docList)  # create vocabulary

    trainingSet = range(50);
    testSet = []  # test셋을 생성해준다

    for i in range(10):
        randIndex = int(random.uniform(0, len(trainingSet)))

        testSet.append(trainingSet[randIndex])

        del (trainingSet[randIndex])

    trainMat = [];
    trainClasses = []

    for docIndex in trainingSet:  # train the classifier (get probs) trainNB0

        trainMat.append(bagOfWords2VecMN(vocabList, docList[docIndex]))

        trainClasses.append(classList[docIndex])

    p0V, p1V, pSpam = trainNB0(array(trainMat), array(trainClasses))

    errorCount = 0

    for docIndex in testSet:  # classify the remaining items

        wordVector = bagOfWords2VecMN(vocabList, docList[docIndex])

        if classifyNB(array(wordVector), p0V, p1V, pSpam) != classList[docIndex]:
            errorCount += 1

            print
            "classification error", docList[docIndex]

    print
    'the error rate is: ', float(errorCount) / len(testSet)

    # return vocabList,fullText


def calcMostFreq(vocabList, fullText):
    import operator

    freqDict = {}

    for token in vocabList:
        freqDict[token] = fullText.count(token)

    sortedFreq = sorted(freqDict.iteritems(), key=operator.itemgetter(1), reverse=True)

    return sortedFreq[:30]


def localWords(feed1, feed0):
    import feedparser

    docList = [];
    classList = [];
    fullText = []

    minLen = min(len(feed1['entries']), len(feed0['entries']))

    for i in range(minLen):
        wordList = textParse(feed1['entries'][i]['summary'])

        docList.append(wordList)

        fullText.extend(wordList)

        classList.append(1)  # NY is class 1

        wordList = textParse(feed0['entries'][i]['summary'])

        docList.append(wordList)

        fullText.extend(wordList)

        classList.append(0)

    vocabList = createVocabList(docList)  # create vocabulary

    top30Words = calcMostFreq(vocabList, fullText)  # remove top 30 words

    for pairW in top30Words:

        if pairW[0] in vocabList: vocabList.remove(pairW[0])

    trainingSet = range(2 * minLen);
    testSet = []  # testset을 만들어준다

    for i in range(20):
        randIndex = int(random.uniform(0, len(trainingSet)))

        testSet.append(trainingSet[randIndex])

        del (trainingSet[randIndex])

    trainMat = [];
    trainClasses = []

    for docIndex in trainingSet:  # train the classifier (get probs) trainNB0

        trainMat.append(bagOfWords2VecMN(vocabList, docList[docIndex]))

        trainClasses.append(classList[docIndex])

    p0V, p1V, pSpam = trainNB0(array(trainMat), array(trainClasses))

    errorCount = 0

    for docIndex in testSet:  # classify the remaining items

        wordVector = bagOfWords2VecMN(vocabList, docList[docIndex])

        if classifyNB(array(wordVector), p0V, p1V, pSpam) != classList[docIndex]:
            errorCount += 1

    print #error비율 구해주기
    'the error rate is: ', float(errorCount) / len(testSet)

    return vocabList, p0V, p1V


def getTopWords(ny, sf):
    import operator

    vocabList, p0V, p1V = localWords(ny, sf)

    topNY = [];
    topSF = []

    for i in range(len(p0V)):

        if p0V[i] > -6.0: topSF.append((vocabList[i], p0V[i]))

        if p1V[i] > -6.0: topNY.append((vocabList[i], p1V[i]))

    sortedSF = sorted(topSF, key=lambda pair: pair[1], reverse=True)

    print
    "SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**"

    for item in sortedSF:
        print
        item[0]

    sortedNY = sorted(topNY, key=lambda pair: pair[1], reverse=True)

    print
    "NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**"

    for item in sortedNY:
        print
        item[0]


testingNB()