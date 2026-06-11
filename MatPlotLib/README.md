-------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Data Visualization using Matplotlib 📊🐍

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 📌 Project Overview :

This project demonstrates the use of **Pandas** and **Matplotlib** for **data exploration and visualization** using data stored in an Excel spreadsheet.

The objective of this case study is to understand how to:

* Read data from Excel files
* Perform basic exploratory data analysis (EDA)
* Sort and inspect datasets
* Visualize data distributions using Matplotlib
* Generate different types of plots for better interpretation of data

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🎯 Problem Statement :

Analyze data stored in an Excel file and create meaningful visualizations using Matplotlib to gain insights into the dataset.

The application focuses on understanding the **Age distribution** of individuals present in the dataset.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 📊 Dataset Information :

The dataset is stored in an Excel file named:

```text id="j6tn5y"
Marvellous.xlsx
```

The dataset contains information about multiple individuals.

### Dataset Features

| Column  | Description                            |
| ------- | -------------------------------------- |
| Name    | Name of the individual                 |
| College | College associated with the individual |
| Mail ID | Email address                          |
| Age     | Age of the individual                  |

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 📂 Repository Structure :

```text id="33jlwm"
Matplotlib-Case-Study/
│
├── MatPlotLib_1.py
├── Marvellous.xlsx
├── README.md
└── Documentation.pdf
```

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

## ⚙️ Application Workflow :

```text id="uv6h6g"
Load Excel Dataset
        ↓
Display Dataset Information
        ↓
Perform Basic Data Exploration
        ↓
Sort Dataset
        ↓
Visualize Age Distribution
        ↓
Generate Statistical Plots
```

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🔍 Data Analysis Performed :

The application performs the following operations:

### 1. Load Dataset

Reads the Excel file using Pandas.

```python id="j5n3oc"
data = pd.read_excel(excel_file)
```

---

### 2. Display Complete Dataset

Prints all records available in the dataset.

---

### 3. Display First Few Records

Displays:

* First 5 rows
* First 4 rows

using:

```python id="2f70lz"
data.head()
```

---

### 4. Display Last Few Records

Displays:

* Last 3 rows
* Last 4 rows

using:

```python id="dzrfdv"
data.tail()
```

---

### 5. Determine Dataset Dimensions

Displays dataset shape:

```python id="03j8p6"
data.shape
```

This provides:

* Number of rows
* Number of columns

---

### 6. Sort Dataset

Sorts records in descending order based on the **Name** column.

```python id="pvgv04"
data.sort_values(['Name'], ascending=False)
```

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 📈 Visualizations Generated :

### 1. Histogram of Age Distribution

```python id="k2bvw7"
data['Age'].plot(kind='hist')
```

#### Purpose

* Understand the frequency distribution of age values.
* Identify commonly occurring age groups.
* Observe variation in the dataset.

#### Insights

The histogram indicates that the majority of individuals fall within the **early twenties to early thirties age range**.

---

### 2. Horizontal Bar Chart

```python id="zhvot2"
data['Age'].plot(kind='barh')
```

#### Purpose

* Compare age values across different records.
* Provide a clear visual representation of age differences.

#### Insights

The horizontal bar chart allows easy comparison of individual age values within the dataset.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🛠️ Technologies Used :

| Technology | Purpose                        |
| ---------- | ------------------------------ |
| Python     | Programming Language           |
| Pandas     | Data Manipulation and Analysis |
| Matplotlib | Data Visualization             |
| Excel      | Data Storage                   |

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

## ▶️ How to Run :

### Install Dependencies

```bash id="nmkh4j"
pip install pandas matplotlib openpyxl
```

### Execute the Program

```bash id="mqzy16"
python MatPlotLib_1.py
```

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 📚 Key Learning Outcomes :

Through this case study, I learned:

* Reading Excel files using Pandas
* Exploring datasets using head(), tail(), and shape()
* Sorting datasets based on specific attributes
* Creating visualizations using Matplotlib
* Understanding histogram plots
* Understanding horizontal bar charts
* Performing basic exploratory data analysis (EDA)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🚀 Future Enhancements :

Potential improvements include:

* Pie charts for categorical distributions
* Line plots for trend analysis
* Scatter plots for relationship analysis
* Box plots for outlier detection
* Statistical summaries using Pandas
* Interactive visualizations using Plotly or Seaborn

-------------------------------------------------------------------------------------------------------------------------------------------------------------------
