import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import tkinter as tk
from tkinter import messagebox

# Load the dataset
titanic_data = pd.read_csv('tested.csv')

# Handle missing values
titanic_data['Age'] = titanic_data['Age'].fillna(titanic_data['Age'].median())
titanic_data['Embarked'] = titanic_data['Embarked'].fillna(titanic_data['Embarked'].mode()[0])

# Convert categorical variables into dummy/indicator variables
titanic_data = pd.get_dummies(titanic_data, columns=['Sex', 'Embarked'])

# Select features and target variable
X = titanic_data[['Pclass', 'Age', 'SibSp', 'Parch', 'Fare', 'Sex_female', 'Sex_male', 'Embarked_C', 'Embarked_Q', 'Embarked_S']]
y = titanic_data['Survived']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Random Forest classifier
clf = RandomForestClassifier(random_state=42)

# Train the classifier
clf.fit(X_train, y_train)

# Predict on the test set
y_pred = clf.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Create a Tkinter window
window = tk.Tk()
window.title("Titanic Survival Prediction")
window.geometry("300x150")

# Function to display accuracy
def show_accuracy():
    messagebox.showinfo("Accuracy", f"Accuracy: {accuracy:.2f}")

# Button to display accuracy
accuracy_button = tk.Button(window, text="Show Accuracy", command=show_accuracy)
accuracy_button.pack(pady=20)

window.mainloop()
