-------------------------------------------------------------------------------------------------------------------------------------------------------------------

📌 Problem Statement :

Given environmental conditions:

Weather (Sunny, Rainy, Overcast)
Temperature (Hot, Mild, Cool)

Predict whether playing outdoors is recommended.

Output
Yes → Play
No → Don't Play

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

📊 Dataset Overview :

The dataset contains historical observations of weather conditions and whether playing was possible.

Features
Feature	Description
Weather	Sunny, Rainy, Overcast
Temperature	Hot, Mild, Cool
Target Variable
Value	Meaning
Yes	Play
No	Don't Play

Example Records:

Weather	Temperature	Play
Sunny	Hot	No
Overcast	Hot	Yes
Rainy	Mild	Yes
Sunny	Cool	Yes

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

🧠 Machine Learning Algorithm :

K-Nearest Neighbors (KNN)

The project uses:

KNeighborsClassifier(n_neighbors=3)

KNN predicts the output by finding the 3 nearest data points and selecting the majority class among them.

Why KNN?
Easy to understand and implement
No explicit training phase
Suitable for small datasets
Excellent algorithm for learning classification fundamentals
⚙️ Data Preprocessing

Since Machine Learning models work with numerical data, categorical values are converted using Label Encoding.

Weather Encoding
Weather	Encoded Value
Overcast	0
Rainy	1
Sunny	2
Temperature Encoding
Temperature	Encoded Value
Cool	0
Hot	1
Mild	2
Target Encoding
Play	Encoded Value
No	0
Yes	1

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

📂 Project Structure :

PlayPredictor/
│
├── PlayPredictor.csv
├── PlayPredictor_1.py
└── README.md
PlayPredictor.csv

Contains training data used by the model.

PlayPredictor_1.py

Implements:

Dataset loading using Pandas
Label Encoding
Feature preparation
KNN model training
Prediction generation

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

🔄 Machine Learning Workflow :

Load dataset
Extract features and labels
Encode categorical values
Train KNN classifier
Predict play possibility for new conditions
Weather + Temperature
          ↓
   Label Encoding
          ↓
      KNN Model
          ↓
      Prediction

-------------------------------------------------------------------------------------------------------------------------------------------------------------------
      
▶️ Running the Project :
 
Install required dependencies:

pip install pandas numpy scikit-learn

Run:

python PlayPredictor_1.py
🎯 Sample Prediction

Input:

Weather     : Overcast
Temperature : Mild

Encoded Input:

[0, 2]

Prediction:

Yes

The model predicts that playing is possible under these conditions.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

📚 Concepts Learned :

Through this project, I learned:

Supervised Learning
Classification Problems
K-Nearest Neighbors (KNN)
Label Encoding
Data Preparation
Model Training
Prediction using Scikit-Learn
Working with CSV datasets using Pandas

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

🚀 Future Improvements :

Potential enhancements:

Add Humidity and Wind features
Increase dataset size
Train-Test Split
Accuracy Evaluation
Confusion Matrix
Cross Validation
User Interactive Input System
Comparison with Decision Tree and Naive Bayes algorithms

-------------------------------------------------------------------------------------------------------------------------------------------------------------------
