# ft_linear_regression 

**An introduction to machine learning through linear regression**

> Predict the price of a car based on its mileage using gradient descent and simple linear regression.

---

## ▌Project Overview

This project is a minimal and educational implementation of **linear regression** using **gradient descent** to predict the price of a car from its mileage.\
It serves as an introduction to **machine learning fundamentals**, written from scratch without using high-level libraries that do the work for you.

📘 Inspired by 42's AI curriculum: **you'll build and train your own model step-by-step**.

<div align="center">

| Prediction line | Loss function curve |
|:---:|:---:|
| <img src="https://github.com/user-attachments/assets/866e813c-1b79-4d84-b42e-78e6e0158870" alt="Prediction line" width="500"> | <img src="https://github.com/user-attachments/assets/f2294f05-e9b6-4f62-9d3c-d4e58a44cade" alt="Loss function curve" width="500"> |

</div>


---


<div align="center">

| Prediction line | Loss function curve |
|:---:|:---:|
| <img src="https://github.com/user-attachments/assets/866e813c-1b79-4d84-b42e-78e6e0158870" alt="Prediction line" width="500"> | <img src="https://github.com/user-attachments/assets/f2294f05-e9b6-4f62-9d3c-d4e58a44cade" alt="Loss function curve" width="500"> |

</div>


## ▌Features

✔️ Linear regression with **one feature** (car mileage)\
✔️ Manual implementation of **gradient descent**\
✔️ Interactive program to predict car prices\
✔️ Model parameters are saved and reused\
✔️ Clean and readable Python code with modular architecture\
✔️ Data visualization and comprehensive model evaluation (Bonus)

---

## ▌How it works

### ■ Method Used

The model is trained using **simple linear regression** with **gradient descent optimization**. The objective is to minimize the **Mean Squared Error (MSE)** between predicted and actual prices.

### ■ Hypothesis function

The model predicts the price using a linear function:

$$
\hat{y} = \theta_0 + \theta_1 \times x
$$

Where:
- $\theta_0$ (theta0) is the y-intercept (bias term)
- $\theta_1$ (theta1) is the slope (coefficient for mileage)
- $x$ is the input feature (mileage)
- $\hat{y}$ is the predicted price
- Initially, both parameters are set to 0 before training

### ■ Training formulas (Gradient Descent)

The model updates parameters using gradient descent to minimize the cost function:

$$
\theta_0 := \theta_0 - \alpha \times \frac{1}{m} \times \sum_{i=0}^{m-1} (\hat{y}_i - y_i)
$$

$$
\theta_1 := \theta_1 - \alpha \times \frac{1}{m} \times \sum_{i=0}^{m-1} ((\hat{y}_i - y_i) \times x_i)
$$

Where:
- $\alpha$ (alpha) is the learning rate
- $m$ is the number of training samples
- $\hat{y}_i = \theta_0 + \theta_1 \times x_i$ is the predicted value
- $y_i$ is the actual value
- The parameters are updated simultaneously after each iteration

### ■ Project Structure

The project follows a modular architecture:

```
ft_linear_regression/
├── model.py              # Model class (training logic)
├── prediction.py         # Prediction program
├── data.py               # Data class (model parameters)
├── data_processing.py    # DataProcessing class (CSV/JSON handling)
├── plotting.py           # Plotting class (visualizations)
├── metrics.py            # Metrics class (precision calculations)
├── datasets/
│   └── data.csv          # Training dataset
└── model/
    └── model.json        # Saved model parameters
```

---

## ▌Getting Started

### ■ Requirements

- Python 3.x
- `matplotlib` (for data visualization)

> ❌ No use of libraries like `numpy`, `scikit-learn`, or `pandas` is allowed.

### ■ Installation & Usage

1. Clone the repository

```bash
git clone https://github.com/ai-dg/ft_linear_regression.git
cd ft_linear_regression
```

2. Train your model

```bash
python3 model.py
```

The model will:
- Initialize parameters θ₀ and θ₁ to 0
- Train for 5000 iterations (default)
- Display MSE evolution during training
- Calculate and display precision metrics
- Save trained parameters to `model/model.json`
- Generate visualization graphs

3. Predict car price by mileage

```bash
python3 prediction.py
```

Enter a mileage value when prompted to get a price prediction.

---

## ▌Model Evaluation Metrics

The model calculates several metrics to evaluate its performance:

### 1. Mean Squared Error (MSE)

Measures the average squared difference between predicted and actual values:

$$
MSE = \frac{1}{m} \sum_{i=0}^{m-1} (\hat{y}_i - y_i)^2
$$

### 2. Root Mean Squared Error (RMSE)

Square root of MSE, in the same units as the target variable:

$$
RMSE = \sqrt{MSE} = \sqrt{\frac{1}{m} \sum_{i=0}^{m-1} (\hat{y}_i - y_i)^2}
$$

### 3. Mean Absolute Error (MAE)

Average absolute difference between predictions and actual values:

$$
MAE = \frac{1}{m} \sum_{i=0}^{m-1} |\hat{y}_i - y_i|
$$

### 4. Mean Absolute Percentage Error (MAPE)

Average percentage error, useful for understanding relative error:

$$
MAPE = \frac{100}{m} \sum_{i=0}^{m-1} \left|\frac{\hat{y}_i - y_i}{y_i}\right|
$$

### 5. R² Score (Coefficient of Determination)

Measures how well the model fits the data (0 to 1, higher is better):

$$
R^2 = 1 - \frac{SS_{res}}{SS_{tot}}
$$

Where:

$$
SS_{res} = \sum_{i=0}^{m-1} (\hat{y}_i - y_i)^2 \quad \text{(Sum of Squares of Residuals)}
$$

$$
SS_{tot} = \sum_{i=0}^{m-1} (y_i - \bar{y})^2 \quad \text{(Total Sum of Squares)}
$$

$$
\bar{y} = \frac{1}{m} \sum_{i=0}^{m-1} y_i \quad \text{(Mean of actual values)}
$$

---

## ▌Example Output

### Training Output

```bash
$ python3 model.py
Iteration: 0/5000 - MSE = 0.16666666666666666
Iteration: 1/5000 - MSE = 0.16423456789012345
...
Iteration: 4999/5000 - MSE = 0.006484555564514827
Iteration: 5000/5000 - MSE = 0.006484555564514827

Final result after 5000 iterations
θ0: 1.0252834318375312
θ1: -0.6209591389636161

**************************************************
PRECISION METRICS
**************************************************
Data size: 24 samples

Error Metrics:
  MSE  (Mean Squared Error):     445645.25
  RMSE (Root Mean Squared Error): 667.57
  MAE  (Mean Absolute Error):     557.84
  MAPE (Mean Absolute % Error):  9.65%

Performance Metrics:
  R²   (Coefficient of Determination): 0.7330

**************************************************
Interpretation:
  - Lower MSE/RMSE/MAE/MAPE = Better model
  - R² closer to 1.0 = Better fit
  - Current R²: 0.7330 (Good)
**************************************************
```

### Prediction Output

```bash
$ python3 prediction.py
Enter your mileage: 50000
Price predicted (50000.0 km): 7205.42
```

---

## ▌Results Interpretation

Based on the training results:

- **R² = 0.7330 (Good)**: The model explains 73.3% of the variance in car prices, indicating a good fit.
- **RMSE = 667.57**: On average, predictions are off by about 668 euros.
- **MAE = 557.84**: The average absolute error is 558 euros.
- **MAPE = 9.65%**: The average percentage error is about 9.65%, which is reasonable for price prediction.

The model shows a **negative correlation** between mileage and price (θ₁ = -0.621), which is expected: cars with higher mileage tend to have lower prices.

---

## ▌Bonus Features

- ✅ **Data visualization**: Graph showing dataset points and the trained regression line
- ✅ **MSE evolution plot**: Real-time display of MSE convergence during training
- ✅ **Comprehensive metrics**: MSE, RMSE, MAE, MAPE, and R² calculation
- ✅ **Robust error handling**: Input validation and file error handling
- ✅ **Reusable model**: Model parameters stored as JSON for reuse

> ⚠️ These features are only evaluated if the core program works flawlessly.

---

## 📜 License

This project was completed as part of the **42 School** curriculum.\
It is intended for **academic purposes only** and follows the evaluation requirements set by 42.

Unauthorized public sharing or direct copying for **grading purposes** is discouraged.\
If you wish to use or study this code, please ensure it complies with **your school's policies**.
