# ft_linear_regression 
**An introduction to machine learning through linear regression**  

> Predict the price of a car based on its mileage using gradient descent and simple linear regression.

---

## ▌Project Overview  

This project is a minimal and educational implementation of **linear regression** using **gradient descent** to predict the price of a car from its mileage.  
It serves as an introduction to **machine learning fundamentals**, written from scratch without using high-level libraries that do the work for you.

📘 Inspired by 42's AI curriculum: **you'll build and train your own model step-by-step**.

---

## ▌Features  

✔️ Linear regression with **one feature** (car mileage)  
✔️ Manual implementation of **gradient descent**  
✔️ Interactive program to predict car prices  
✔️ Model parameters are saved and reused  
✔️ Clean and readable Python code  
✔️ Optional data visualization and model evaluation (Bonus)

---

## ▌How it works  

### ■ Hypothesis function  
The model is based on the simple linear formula:  
```text
estimatePrice(mileage) = theta0 + theta1 * mileage

Initially, theta0 and theta1 are set to 0.
Training is performed using gradient descent to minimize the cost between predicted and actual prices.
```


## ■ Training formulas
```txt
theta0 -= learningRate * (1/m) * Σ(estimatePrice(x_i) - y_i)
theta1 -= learningRate * (1/m) * Σ((estimatePrice(x_i) - y_i) * x_i)
```

## ▌Getting Started
### ■ Requirements
▸ Python 3.x
▸ matplotlib (optional, for plotting bonus)
▸ No use of libraries like numpy.polyfit or sklearn is allowed

### ■ Installation & Usage
1. Clone the repository
```bash
git clone https://github.com/ai-dg/ft_linear_regression.git
cd ft_linear_regression
```
2. Train your model
```bash
python3 train.py
```
3. Predict car price by mileage
```bash
python3 predict.py
```

## ▌Bonus Features
✔️ Graph showing the dataset points and the trained regression line
✔️ Model evaluation (e.g. mean squared error)
✔️ Robust error handling for inputs
✔️ Reusable model saved as JSON

These are only evaluated if the core program works flawlessly.


## ▌Example
```bash
$ python3 train.py
Training complete! Thetas saved in theta.json

$ python3 predict.py
Enter mileage: 50000
Estimated price: €11,378.24
```

## 📜 License

This project was completed as part of the **42 School** curriculum.  
It is intended for **academic purposes only** and follows the evaluation requirements set by 42.  

Unauthorized public sharing or direct copying for **grading purposes** is discouraged.  
If you wish to use or study this code, please ensure it complies with **your school's policies**.
