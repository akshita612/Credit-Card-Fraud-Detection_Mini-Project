# -*- coding: utf-8 -*-
"""logistic.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/173vJP9EAsXNDm4A45x-DAg3MV_3D7QTP
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Loading the dataset to a Pandas DataFrame
credit_card_data = pd.read_csv('creditcard.csv')

# Dataset information
credit_card_data.info()

credit_card_data.isnull().sum()

# Displaying the last 5 rows of the dataset
print('The last 5 rows of the dataset:')
credit_card_data.tail()

# Distribution of legit transactions and fraudulent transactions
credit_card_data['Class'].value_counts()

# Separating the data for analysis
legit = credit_card_data[credit_card_data.Class == 0]
fraud = credit_card_data[credit_card_data.Class == 1]
print(legit.shape)
print(fraud.shape)

# Statistical measures for this data (legit transactions)
legit.Amount.describe()

# Statistical measures for this data (fraudulent transactions)
fraud.Amount.describe()

# Comparing the values for both transactions
credit_card_data.groupby('Class').mean()

# Randomly selecting 492 transactions from the legit transactions and concatenating two DataFrames
legit_sample = legit.sample(n=492)
new_dataset = pd.concat([legit_sample,fraud],axis=0)

# Displaying the first 5 rows of the new dataset
new_dataset.head()

# Displaying the last 5 rows of the new dataset
new_dataset.tail()

# Distribution of legit transactions and fraudulent transactions in the new dataset
new_dataset['Class'].value_counts()

# Comparing the values for both transactions in the new dataset
new_dataset.groupby('Class').mean()

# Splitting the new dataset into features(X) and targets/labels(Y)
X = new_dataset.drop(columns='Class',axis=1)
Y = new_dataset['Class']
print('Features:\n',X)
print('Targets/Labels:\n',Y)

# Splitting the features and labels to training data and test data (arrays)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)
print(X.shape, X_train.shape, X_test.shape)
print(Y.shape, Y_train.shape, Y_test.shape)

# Loading one instance of Logistic Regression model
model = LogisticRegression()

# Training the Logistic Regression model with training data (X_train, Y_train)
model.fit(X_train,Y_train)

# Predicting all the labels corresponding X_train data
X_train_prediction = model.predict(X_train)

# Accuracy on training data by comparing the values predicted by our model (X_train_prediction) with the original values (X_train)
training_model_accuracy = accuracy_score(X_train_prediction,Y_train)

# Predicting all the labels corresponding X_test data
X_test_prediction = model.predict(X_test)

# Accuracy on test data by comparing the values predicted by our model (X_test_prediction) with the original values (X_test)
test_model_accuracy = accuracy_score(X_test_prediction,Y_test)

print('The Accuracy of the Training data: {}\nIn Percentage = {}\n'.format(training_model_accuracy, training_model_accuracy*100))
print('The Accuracy of the Test data: {}\nIn Percentage = {}'.format(test_model_accuracy, test_model_accuracy*100))

# Creating a new DataFrame
accuracy_percentage = {
    'Model': ['Training Model','Test Model'],
    'Percentage': [training_model_accuracy*100,test_model_accuracy*100]
}
df = pd.DataFrame(accuracy_percentage)
df

# Plotting the Bar graph showing the comparison between the Accuracies of Training and Test models
plt.figure(figsize=(8, 6))
plots = sns.barplot(x="Model", y="Percentage",data=df)
for bar in plots.patches:
    plots.annotate(
        format(bar.get_height(), '.2f'), (bar.get_x() + bar.get_width()/2, 
                bar.get_height()), ha='center', va='center',
                size=15, xytext=(0, 8),
                textcoords='offset points'
    )
plt.title("Comparison between the Accuracies of Training and Test models")
plt.xlabel("Model")
plt.ylabel("Accuracy Percentage(%)")
plt.show()