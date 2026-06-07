-------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Ball Type Prediction using Machine Learning 🎾🏏

A simple Machine Learning case study that uses a **Decision Tree Classifier** to identify whether a given ball is a **Tennis Ball** or a **Cricket Ball** based on its physical characteristics.

This project was created as part of my Machine Learning learning journey to understand the complete workflow of:

* Dataset preparation
* Feature encoding
* Model training
* Prediction
* User interaction

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 📌 Problem Statement

Given the following properties of a ball:

* **Weight (grams)**
* **Surface Pattern (Rough / Smooth)**

Predict whether the ball is:

* 🎾 Tennis Ball
* 🏏 Cricket Ball

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 📊 Dataset

The training dataset contains examples of Tennis and Cricket balls with their corresponding weight and surface pattern.

| Weight | Pattern | Label   |
| ------ | ------- | ------- |
| 35     | Rough   | Tennis  |
| 47     | Rough   | Tennis  |
| 90     | Smooth  | Cricket |
| 48     | Rough   | Tennis  |
| 92     | Smooth  | Cricket |
| 96     | Smooth  | Cricket |
| 110    | Smooth  | Cricket |

Feature Encoding:

| Feature | Value |
| ------- | ----- |
| Rough   | 1     |
| Smooth  | 0     |

Label Encoding:

| Label   | Value |
| ------- | ----- |
| Tennis  | 1     |
| Cricket | 2     |

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🧠 Machine Learning Algorithm

The project uses:

**Decision Tree Classifier**

from the Scikit-Learn library.

Why Decision Tree?

* Easy to understand
* Suitable for small datasets
* Handles classification problems effectively
* Useful for learning Machine Learning fundamentals

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 📂 Repository Contents

### BallCase1.py

* Basic implementation using textual labels
* Direct training and prediction

### BallCase2.py

* Introduces numerical encoding for features and labels
* Improves compatibility with Machine Learning algorithms

### BallCase3.py

* Modular implementation using functions
* Separates training and prediction logic

### BallCase4.py

* Interactive version
* Accepts user input for weight and surface type
* Predicts whether the object resembles a Tennis Ball or Cricket Ball

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

## ⚙️ Installation

Install Scikit-Learn:

```bash
pip install scikit-learn
```

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

## ▶️ Running the Project

Execute the interactive version:

```bash
python BallCase4.py
```

Example:

```text
Please enter the weight of your object in grams
97

Please enter the type of surface of your object
Smooth
```

Output:

```text
Your object looks like a Cricket ball
```

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🎯 Learning Outcomes

Through this project, I learned:

* Supervised Machine Learning
* Classification Problems
* Feature and Label Encoding
* Decision Tree Algorithms
* Model Training using Scikit-Learn
* Making Predictions on New Data
* Building Interactive ML Applications

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🚀 Future Improvements

Possible enhancements:

* Larger training dataset
* Additional ball categories
* Accuracy evaluation metrics
* Train-Test Split
* Graphical Visualization of Decision Tree
* Support for multiple Machine Learning algorithms

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 👨‍💻 Author

**Pratik Chavan**

Software Developer

This project was developed as a beginner-friendly Machine Learning case study to understand how classification models learn patterns from data and make predictions on unseen inputs.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------
