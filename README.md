# 🚗 Automobile Data Analysis – Toyota Cars

This project performs **Exploratory Data Analysis (EDA)** on a dataset of Toyota cars using Python. It covers price, mileage, engine details, and car body style to uncover patterns and insights in automotive features and pricing.

---

## 📊 Dataset Overview

The dataset includes the following features:

- `company`: Manufacturer (Toyota)
- `body-style`: Car body type (e.g., hatchback, wagon)
- `wheel-base`: Distance between wheels
- `length`: Overall length of the car
- `engine-type`: Engine category (e.g., ohc)
- `num-of-cylinders`: Number of engine cylinders
- `horsepower`: Engine power
- `average-mileage`: Fuel efficiency (mpg)
- `price`: Market price in USD

---

## 🧠 Objectives

- Clean and understand the dataset
- Analyze price distribution by car body style
- Investigate how horsepower affects price
- Identify correlations between numerical features

---

## 📈 Visual Insights

### 🔹 1. Car Price by Body Style
![Car Price by Body Style](images/price_by_bodystyle.png)

---

### 🔹 2. Horsepower vs Price
![Horsepower vs Price](images/horsepower_vs_price.png)

---

### 🔹 3. Feature Correlation Heatmap
![Feature Correlation](images/correlation_heatmap.png)

---

## 📝 Key Insights

- **Wagons** tend to have higher prices than **hatchbacks**.
- **Horsepower** is positively correlated with **price**.
- No strong correlation was observed between **average mileage** and **price**.
- Most cars in this dataset have the **same engine type and cylinder count**, indicating a narrow product range.

---

## 🛠️ Tech Stack

- **Python 3**
- **Pandas**
- **Matplotlib / Seaborn**
- **Jupyter Notebook or .py script**

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python automobile_analysis.py
```

---

## 📁 Folder Structure

```
AutoMobile-Analysis/
├── README.md
├── requirements.txt
├── automobile_analysis.py
├── Auto_Mobile_Data.xlsx
├── images/
│   ├── price_by_bodystyle.png
│   ├── horsepower_vs_price.png
│   └── correlation_heatmap.png
```

---

## 🧾 License

This project is for educational use.

