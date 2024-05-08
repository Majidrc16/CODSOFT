import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

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

# Initialize the Random Forest classifier
clf = RandomForestClassifier(random_state=42)

# Train the classifier
clf.fit(X, y)

# Create a Tkinter window
window = tk.Tk()
window.title("Titanic Survival Prediction")

# Function to predict survival
def predict_survival():
    pclass = int(entry_pclass.get())
    age = float(entry_age.get())
    sibsp = int(entry_sibsp.get())
    parch = int(entry_parch.get())
    fare = float(entry_fare.get())
    sex = int(var_sex.get())
    embarked = int(var_embarked.get())
    
    prediction = clf.predict([[pclass, age, sibsp, parch, fare, 0, sex, embarked, 0, 0]])
    
    if prediction[0] == 1:
        result = "Survived"
    else:
        result = "Did not survive"
    
    messagebox.showinfo("Prediction", f"The passenger {result}")

# Function to apply CSS-like styling
def apply_style(widget, bg, fg, font):
    widget.configure(background=bg, foreground=fg, font=font)

# Create entry fields for each feature
bg_color = "#f0f0f0"
fg_color = "black"
font_style = ("Arial", 10)

tk.Label(window, text="Pclass").grid(row=0, column=0, padx=10, pady=5)
entry_pclass = ttk.Entry(window)
entry_pclass.grid(row=0, column=1, padx=10, pady=5)
apply_style(entry_pclass, bg_color, fg_color, font_style)

tk.Label(window, text="Age").grid(row=1, column=0, padx=10, pady=5)
entry_age = ttk.Entry(window)
entry_age.grid(row=1, column=1, padx=10, pady=5)
apply_style(entry_age, bg_color, fg_color, font_style)

tk.Label(window, text="SibSp").grid(row=2, column=0, padx=10, pady=5)
entry_sibsp = ttk.Entry(window)
entry_sibsp.grid(row=2, column=1, padx=10, pady=5)
apply_style(entry_sibsp, bg_color, fg_color, font_style)

tk.Label(window, text="Parch").grid(row=3, column=0, padx=10, pady=5)
entry_parch = ttk.Entry(window)
entry_parch.grid(row=3, column=1, padx=10, pady=5)
apply_style(entry_parch, bg_color, fg_color, font_style)

tk.Label(window, text="Fare").grid(row=4, column=0, padx=10, pady=5)
entry_fare = ttk.Entry(window)
entry_fare.grid(row=4, column=1, padx=10, pady=5)
apply_style(entry_fare, bg_color, fg_color, font_style)

var_sex = tk.IntVar()
tk.Label(window, text="Sex").grid(row=5, column=0, padx=10, pady=5)
tk.Radiobutton(window, text="Male", variable=var_sex, value=0).grid(row=5, column=1, padx=10, pady=5)
tk.Radiobutton(window, text="Female", variable=var_sex, value=1).grid(row=5, column=2, padx=10, pady=5)

var_embarked = tk.IntVar()
tk.Label(window, text="Embarked").grid(row=6, column=0, padx=10, pady=5)
tk.Radiobutton(window, text="C", variable=var_embarked, value=1).grid(row=6, column=1, padx=10, pady=5)
tk.Radiobutton(window, text="Q", variable=var_embarked, value=2).grid(row=6, column=2, padx=10, pady=5)
tk.Radiobutton(window, text="S", variable=var_embarked, value=3).grid(row=6, column=3, padx=10, pady=5)

# Button to predict survival
predict_button = ttk.Button(window, text="Predict", command=predict_survival)
predict_button.grid(row=7, columnspan=2, pady=10)

window.mainloop()
