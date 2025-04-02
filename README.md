# ft_linear_regression 

<img src="https://github.com/user-attachments/assets/866e813c-1b79-4d84-b42e-78e6e0158870" width="500">

<img src="https://github.com/user-attachments/assets/f2294f05-e9b6-4f62-9d3c-d4e58a44cade" width="500">

**An introduction to machine learning through linear regression**

> Predict the price of a car based on its mileage using gradient descent and simple linear regression.

---

## ▌Project Overview

This project is a minimal and educational implementation of **linear regression** using **gradient descent** to predict the price of a car from its mileage.\
It serves as an introduction to **machine learning fundamentals**, written from scratch without using high-level libraries that do the work for you.

📘 Inspired by 42's AI curriculum: **you'll build and train your own model step-by-step**.

---

## ▌Features

✔️ Linear regression with **one feature** (car mileage)\
✔️ Manual implementation of **gradient descent**\
✔️ Interactive program to predict car prices\
✔️ Model parameters are saved and reused\
✔️ Clean and readable Python code\
✔️ Optional data visualization and model evaluation (Bonus)

---

## ▌How it works

### ■ Method Used

The model is trained using **simple linear regression** with **gradient descent optimization**. The objective is to minimize the **Mean Squared Error (MSE)** between predicted and actual prices.

### ■ Hypothesis function

```text
estimatePrice(mileage) = theta0 + theta1 * mileage
```

- Initially, `theta0` and `theta1` can be set to 0 for visualizing convergence.
- Training is performed using gradient descent to minimize the cost.

### ■ Training formulas

```text
theta0 -= learningRate * (1/m) * Σ(estimatePrice(x_i) - y_i)
theta1 -= learningRate * (1/m) * Σ((estimatePrice(x_i) - y_i) * x_i)
```

---

## ▌Getting Started

### ■ Requirements

- Python 3.x
- `matplotlib` (optional, for plotting bonus)

> ❌ No use of libraries like `numpy`, `scikit-learn`, or `pandas` is allowed.

### ■ Installation & Usage

1. Clone the repository

```bash
git clone https://github.com/ai-dg/ft_linear_regression.git
cd ft_linear_regression
```

2. (Optional) Edit `values.json` to start from scratch:

```json
{
  "theta0": 0,
  "theta1": 0,
  "max_km": 240000,
  "max_price": 8290.0
}
```

This allows you to visualize the evolution of `theta0`, `theta1`, and the MSE.

3. Train your model

```bash
python3 model.py
```

4. Predict car price by mileage

```bash
python3 prediction.py
```

---

## ▌Bonus Features

- ■ Graph showing the dataset points and the trained regression line
- ■ Real-time MSE display and convergence plot
- ■ Robust input and file error handling
- ■ Reusable model stored as JSON

> ⚠️ These features are only evaluated if the core program works flawlessly.

---

## ▌Example

```bash
$ python3 model.py
Iteration 0: theta0 = 0.076, theta1 = 0.029
...
Iteration 9000: theta0 = 1.02528, theta1 = -0.62095
Entraînement terminé. Paramètres sauvegardés.
MAE (Erreur absolue moyenne) : 557.84 €

$ python3 prediction.py
Enter mileage: 50000
Estimated price: €11,378.24
```

---

## 📜 License

This project was completed as part of the **42 School** curriculum.\
It is intended for **academic purposes only** and follows the evaluation requirements set by 42.

Unauthorized public sharing or direct copying for **grading purposes** is discouraged.\
If you wish to use or study this code, please ensure it complies with **your school's policies**.

