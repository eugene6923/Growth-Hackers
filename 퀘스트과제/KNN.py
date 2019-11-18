import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from os import listdir
from IPython.display import display

training_file_list = listdir('D:\\그로스해커스\\KNN\\data\\trainingDigits')
test_file_list = listdir('D:\\그로스해커스\\KNN\\data\\testDigits')

# 1번
def function(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        dataset = file.readlines()
        data = []
        for i in range(len(dataset)):
            data += dataset[i].rstrip()
        result = np.array(data)
        return(result)

# 2번
def functionY(file_name):
    return(file_name[0])

# 3번
X_train = []
Y_train = []
X_test = []
Y_test = []

for file_name in training_file_list:
    X_train.append(function('D:\\그로스해커스\\KNN\\data\\trainingDigits'+ '\\' + file_name))
    Y_train.append(functionY(file_name))

for file_name in test_file_list:
    X_test.append(function('D:\\그로스해커스\\KNN\\data\\testDigits'+'\\' + file_name))
    Y_test.append(functionY(file_name))

X_train = np.array(X_train).astype(np.int32)
Y_train = np.array(Y_train).astype(np.int32)
X_test = np.array(X_test).astype(np.int32)
Y_test = np.array(Y_test).astype(np.int32)

# 4번
from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X_train, Y_train, test_size=0.3, random_state=0)

# 5번
from sklearn.neighbors import KNeighborsClassifier

KNN = []
for i in range(10):
    knn = KNeighborsClassifier(n_neighbors=i+1)
    knn.fit(X_train, Y_train)
    KNN.append(knn.score(X_train, Y_train))

print(min(KNN))
#0.9887892376681614가 최소로 print 된다.

plt.scatter(range(1,11), KNN)
plt.show()