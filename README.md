# Titanic Survival Prediction
This project predicts the survival of passengers aboard the Titanic using machine learning techniques. It utilizes the Random Forest Classifier algorithm and includes a Tkinter GUI for displaying accuracy.

# Files:
titanic_survival_prediction.py: Python script containing the code for data preprocessing, model training, and creating a Tkinter GUI for displaying accuracy.
tested.csv: Dataset containing Titanic passenger information.

# Dependencies:
Python 3.x
pandas
scikit-learn
tkinter

# Usage:
Install Dependencies:Ensure you have Python installed on your system. Install the required libraries using pip:
``
pip install pandas scikit-learn
``

Clone the Repository:
``
bash
git clone <repository-url>
``
``
Run the Script:

python titanic_survival_prediction.py
``

This script preprocesses the data, trains the Random Forest classifier, and creates a Tkinter window to display the accuracy of the model.
Interact with the GUI:Once the script is running, a Tkinter window will appear. Click the "Show Accuracy" button to display the accuracy of the model on the test dataset.
# Dataset:
The dataset used (tested.csv) contains passenger information such as age, gender, class, and survival status.
Missing values in the dataset are handled by replacing missing ages with the median age and missing embarked values with the mode.
Categorical variables like 'Sex' and 'Embarked' are converted into dummy/indicator variables.

# Notes:
You can modify the script or dataset to experiment with different features or algorithms.
Feel free to customize the GUI or extend the functionality as needed.

