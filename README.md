# 🛍 Customer Segmentation System using Machine Learning

## 📌 Project Overview

This project is a **Customer Segmentation System** built using **K-Means Clustering** and deployed as a **Flask web application**.

The system groups customers based on their **Annual Income** and **Spending Score**, helping businesses understand customer behavior and target them effectively.

---

## 🎯 Objectives

* Segment customers into different groups
* Identify high-value and low-value customers
* Support marketing and business decision-making
* Provide an interactive web interface for predictions

---

## 📊 Dataset

* Dataset used: **Mall Customers Dataset**
* Source: Kaggle
* Link: https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python

---

## 📁 Dataset Features

| Feature                | Description                      |
| ---------------------- | -------------------------------- |
| CustomerID             | Unique ID of customer            |
| Gender                 | Male/Female                      |
| Age                    | Age of customer                  |
| Annual Income (k$)     | Income in thousand dollars       |
| Spending Score (1-100) | Score assigned based on behavior |

---

## ⚙️ How the System Works

1. User enters:

   * Annual Income (₹)
   * Spending Score (1–100)

2. System converts:

   * ₹ → k$ (for model compatibility)

3. Model:

   * Uses **K-Means Clustering**
   * Groups customers into 5 segments

4. Output:

   * Displays customer segment
   * Shows visualization with clusters and user position

---

## 🧠 Machine Learning Model

* Algorithm: **K-Means Clustering**
* Type: **Unsupervised Learning**
* Number of clusters: **5**
* Optimization: **Elbow Method**

---

## 📊 Visualization

* Scatter plot of customer clusters
* Centroids (cluster centers)
* User input highlighted on graph

---

## 🏗 Project Architecture

```text
User Input (Web UI)
        ↓
Flask Backend (app.py)
        ↓
Model Prediction (K-Means)
        ↓
Output + Visualization
```

---

## 📂 Project Structure

```text
project/
│
├── Mall_Customers.csv
├── model.py
├── model.pkl
├── app.py
└── templates/
    └── index.html
```

---

## 🧪 Model Performance

* Since this is an **unsupervised model**, accuracy is not measured traditionally
* Performance evaluated using:

  * **Cluster separation**
  * **Elbow Method (WCSS)**
  * Visual inspection of clusters

---

## 📦 Required Python Libraries

* pandas
* numpy
* scikit-learn
* matplotlib
* flask
* pickle

---

## ⚙️ Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/AlokRana01/Customer-Segmentation-System-using-Machine-Learning.git
```

### 2. Install Dependencies

```bash
pip install pandas numpy scikit-learn matplotlib flask
```

### 3. Train Model

```bash
python model.py
```

### 4. Run Application

```bash
python app.py
```

### 5. Open Browser

```
http://127.0.0.1:5000/
```

---

## 💡 Features

* Clean and minimal UI
* Real-time prediction
* ₹ to $ conversion support
* Cluster visualization
* Highlighted user input point

---

## 🎤 Viva Explanation

* Uses **K-Means clustering** for segmentation
* Groups customers based on behavior
* Helps businesses identify target customers
* Web app built using Flask for usability

---

## 🚀 Future Improvements

* Add interactive graphs (Plotly)
* Deploy on cloud (Heroku / Render)
* Add more features (Age, Gender)
* Improve UI with dashboard

---

## 👨‍💻 Author

Alok Rana

---

## 📌 Conclusion

This project demonstrates how **Machine Learning + Web Development** can be combined to solve real-world business problems like customer segmentation.

---
