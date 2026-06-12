# Deeper into Supervised Learning

In supervised learning, you are acting as the teacher. You provide a dataset with **features** (the inputs, often denoted as $X$) and **labels** (the correct answers, denoted as $y$). The model's job is to find the mathematical mapping function:

$$y = f(X)$$

so that it can predict $y$ for new, unseen data.

Supervised learning generally splits into two main categories based on the type of output you want:

---

## A. Regression (Predicting a Number)

You use regression when the output is a continuous numerical value.

* **How it works:** The algorithm tries to draw a line (or a complex curve) that best fits the data points. It does this by calculating the error between its prediction and the actual answer, often using a formula like **Mean Squared Error (MSE)**:

$$MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$

* **Mechanism:** It then adjusts its internal math to make that error as close to zero as possible.
* **Classic Algorithms:** Linear Regression, Random Forest Regressor.

---

## B. Classification (Predicting a Category)

You use classification when the output is a distinct category or class (e.g., *"Yes/No"*, *"Red/Green/Blue"*).

* **How it works:** Instead of fitting a line through the data, the algorithm tries to draw a decision boundary line between the data points to separate the different classes.
* **Classic Algorithms:** Logistic Regression, Support Vector Machines (SVM), Decision Trees.
