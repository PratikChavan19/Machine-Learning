# Head-Brain Weight Prediction using Linear Regression 🧠📈

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 📌 Project Overview :

This project explores **Simple Linear Regression** by analyzing the relationship between **human head size** and **brain weight**. The primary objective is to understand how regression algorithms model continuous data and how the same problem can be solved using both a **user-defined implementation** and **Scikit-Learn's built-in Linear Regression model**.

The repository demonstrates:

* Linear Regression using the **Least Squares Method**
* Calculation of **Slope** and **Intercept** manually
* Visualization of the **Regression Line**
* Evaluation using the **R² (Coefficient of Determination) Score**
* Linear Regression using **Scikit-Learn**

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🎯 Problem Statement :

Determine the relationship between **Head Size** and **Brain Weight** using Linear Regression.

The model aims to answer the question:

> *Can brain weight be estimated based on head size?*

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 📊 Dataset Information :

The dataset contains information related to human characteristics and brain measurements. According to the case study documentation, it consists of **237 observations**.

### Dataset Features

| Feature              | Description                |
| -------------------- | -------------------------- |
| Gender               | Encoded gender information |
| Age Range            | Encoded age category       |
| Head Size (cm³)      | Volume of the head         |
| Brain Weight (grams) | Weight of the brain        |

For this case study, the model focuses on:

### Input Feature

* Head Size (cm³)

### Target Variable

* Brain Weight (grams)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 📂 Repository Structure :

```text id="34x77d"
Head-Brain-Case-Study/
│
├── HeadBrain_1.py                # Linear Regression from scratch
├── HeadBrain_2.py                # Linear Regression using Scikit-Learn
├── MarvellousHeadBrain.csv       # Dataset
└── README.md
```

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

## ⚙️ Case Study 1: Linear Regression from Scratch :

### Objective

Understand the mathematics behind Linear Regression by implementing it without using Machine Learning libraries.

### Concepts Implemented

* Mean calculation
* Least Squares Method
* Slope calculation
* Y-Intercept calculation
* Regression line generation
* Scatter plot visualization
* R² score computation

### Regression Equation

The model follows:

```text id="o3zndh"
y = mx + c
```

Where:

* **y** → Predicted Brain Weight
* **m** → Slope of Regression Line
* **x** → Head Size
* **c** → Y-Intercept

### Workflow

```text id="nghn1p"
Load Dataset
      ↓
Extract Head Size and Brain Weight
      ↓
Compute Means
      ↓
Calculate Slope and Intercept
      ↓
Generate Regression Line
      ↓
Visualize Results
      ↓
Evaluate using R² Score
```

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🤖 Case Study 2: Linear Regression using Scikit-Learn :

### Algorithm Used

* Linear Regression

### Workflow

1. Load dataset
2. Prepare feature and target variables
3. Reshape input data
4. Train Linear Regression model
5. Generate predictions
6. Calculate R² score

### Concepts Learned

* Working with Scikit-Learn estimators
* Model fitting
* Prediction generation
* Regression evaluation

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 📉 Data Visualization :

The project visualizes:

* Actual data points using a **scatter plot**
* Predicted relationship using a **regression line**

The graph illustrates a **positive linear relationship** between head size and brain weight, indicating that larger head sizes tend to correspond with higher brain weights. The visualization is generated using Matplotlib.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 📈 Model Evaluation :

The goodness of fit is evaluated using the **R² Score**.

### Interpretation

| R² Score        | Meaning                                     |
| --------------- | ------------------------------------------- |
| 0               | Model explains none of the variance         |
| 1               | Perfect prediction                          |
| Between 0 and 1 | Degree to which the model explains the data |

The manually implemented model computes the R² score using the formula:

```text id="g7gf9r"
R² = 1 - (SSR / SST)
```

Where:

* **SSR** = Sum of Squared Residuals
* **SST** = Total Sum of Squares

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🧠 Key Learning Outcomes :

Through this case study, I learned:

* Supervised Learning concepts
* Regression problems
* Linear Regression mathematics
* Least Squares optimization
* Data visualization using Matplotlib
* Model evaluation using R² score
* Implementing ML algorithms from scratch
* Using Scikit-Learn for regression tasks

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

## ▶️ How to Run :

### Install Dependencies

```bash id="ayyu6k"
pip install pandas numpy matplotlib scikit-learn
```

### Run User-Defined Linear Regression

```bash id="gsv59v"
python HeadBrain_1.py
```

### Run Scikit-Learn Linear Regression

```bash id="0wdt2k"
python HeadBrain_2.py
```

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🔄 Comparison of Implementations :

| Aspect                     | User-Defined | Scikit-Learn |
| -------------------------- | ------------ | ------------ |
| Mathematical Understanding | ✅            | ❌            |
| Ease of Implementation     | ❌            | ✅            |
| Visualization              | ✅            | ❌            |
| R² Evaluation              | ✅            | ✅            |
| Production Readiness       | ❌            | ✅            |

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🚀 Future Enhancements :

Potential improvements include:

* Multiple Linear Regression using all available features
* Train-Test Split for better evaluation
* Mean Squared Error (MSE) analysis
* Root Mean Squared Error (RMSE)
* Cross-validation
* Prediction for unseen data
* Interactive user input system

-------------------------------------------------------------------------------------------------------------------------------------------------------------------
This project was developed to understand both the theoretical foundations and practical implementation of Linear Regression by comparing a custom-built approach with Scikit-Learn's industry-standard implementation.
