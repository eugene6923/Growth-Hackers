import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer

#데이터 체크하기
cancer = load_breast_cancer()
print(cancer.keys())
print("유방암 데이터의 형태: {}".format(cancer.data.shape))
print("클래스별 샘플 개수:\n{}".format({n: v for n, v in zip(cancer.target_names, np.bincount(cancer.target))}))
print("특성이름:\n{}".format(cancer.feature_names))

#변수와 결과로 나누기
feature_names = cancer['feature_names']
features = cancer['data']
label_names = cancer['target_names']
labels = cancer['target']

#training test 샘플로 나누기
from sklearn.model_selection import train_test_split
train, test, train_labels, test_labels = train_test_split(features, labels, test_size=0.33,random_state=42)

#성능 비교
from sklearn import metrics

def measure_performance(X, y, clf, show_accuracy=True, show_classification_report=True, show_confusion_matrix=True) :
    y_pred = clf.predict(X)
    if show_accuracy:
        print("Accuraty:{0:.3f}".format(metrics.accuracy_score(y,y_pred),"\n"))
    if show_classification_report:
        print("Classification report")
        print(metrics.classification_report(y,y_pred),"\n")
    if show_confusion_matrix:
        print("Confusion matrix")
        print(metrics.confusion_matrix(y,y_pred),"\n")

from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier

without_random= DecisionTreeClassifier(max_depth=2,random_state=42)
descision = without_random.fit(train,train_labels)
with_random=RandomForestClassifier(max_depth=2,random_state=42)
random=with_random.fit(train,train_labels)

measure_performance(train,train_labels,descision)
measure_performance(train,train_labels,random)