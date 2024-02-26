"""Predicting AQI through traffic,upcoming public events, using 
    Logistic Regression,
    Random forest,
    Support Vector Machine (SVM),
    Naive Bayes,
    K-Neighbors,
    Decision tree 
    
    and test accuracy using formula
    
    Accuracy = No. of Correct Prediction /Size of Dataset or ,
 (True Positives (TP) + True Negatives (TN ))/( True Positives (TP) + True Negatives (TN )
+ False Positives (FP) + False Negatives (FN ))
    
    
    
    This code will load the dataset, split it into training and testing sets, scale the features, 
    initialize classifiers, train them, and evaluate their accuracy. Finally, 
    it will calculate the overall accuracy using the provided formula.
        
    """







import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load dataset
# Assuming you have a dataset with features like traffic, upcoming public events, and the target variable AQI
# Replace 'your_dataset.csv' with the path to your dataset
data = pd.read_csv('your_dataset.csv')

# Preprocessing
X = data.drop(columns=['AQI'])  # Features
y = data['AQI']  # Target variable

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Initialize classifiers
classifiers = {
    'Logistic Regression': LogisticRegression(),
    'Random Forest': RandomForestClassifier(),
    'Support Vector Machine': SVC(),
    'Naive Bayes': GaussianNB(),
    'K-Nearest Neighbors': KNeighborsClassifier(),
    'Decision Tree': DecisionTreeClassifier()
}

# Train and evaluate classifiers
accuracies = {}
for name, classifier in classifiers.items():
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    accuracies[name] = accuracy_score(y_test, y_pred)

# Print accuracy of each classifier
for name, accuracy in accuracies.items():
    print(f'{name}: Accuracy = {accuracy}')

# Calculate overall accuracy using the formula
total_correct_predictions = sum(y_test == y_pred for y_pred in y_test)
total_predictions = len(y_test)
overall_accuracy = total_correct_predictions / total_predictions
print(f'Overall Accuracy using formula: {overall_accuracy}')