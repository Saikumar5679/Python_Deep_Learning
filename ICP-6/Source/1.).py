#import packages for datasets,metrics,Gaussian NB model and test for training data
from sklearn import datasets,metrics
import pandas as pd
import csv
from sklearn import svm
from sklearn.naive_bayes import GaussianNB
#from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
from sklearn import datasets

#load the iris datasets
#irisdatasets=csv.reader("E:\1_Python_icp\'s\ICP-6\Python_Lesson6\iris.csv",delimiter=',')
irisdatasets=datasets.load_iris()
#load the irisdatasets column values
x=irisdatasets.data
y=irisdatasets.target

#split the data for training and testing cross validation
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
#define the model
model=GaussianNB()
#fit the training data into model
model.fit(x_train,y_train)
#prints the probability of training data
#print(model.score(x_train,y_train))
#define to predict the test data
y_pred = model.predict(x_test)
#calc accuracy
print("Accuracy : ",metrics.accuracy_score(y_test, y_pred))
print(y_pred)
#calc precision
#print("Precision:",metrics.precision_score(y_test,y_pred,average='weighted'))
#calc Recall
#print("Recall:",metrics.recall_score(y_test,y_pred,average='weighted'))
#calc F1 score
#print("F1 Score:",metrics.f1_score(y_test,y_pred,average='weighted'))