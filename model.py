import json
import csv
import matplotlib

matplotlib.use("GTK3Agg")
import matplotlib.pyplot as plt

class Data(object):
    theta0: float
    theta1: float
    max_km: float
    max_price: float

    def __init__(self, theta0=0, theta1=0, max_km=0, max_price=0):
        self.theta0 = theta0
        self.theta1 = theta1
        self.max_km = max_km
        self.max_price = max_price

    def update_max_values(self, max_km, max_price):
        self.max_km = max_km
        self.max_price = max_price

    def __str__(self):
        return f"Theta0: {self.theta0}\nTheta1: {self.theta1}\nmax_km: {self.max_km}\nmax_price: {self.max_price}"


def getting_max_values_from_data_csv(path):
    data = []
    max_km = 0
    max_price = 0
    try:
        with open(path) as file:
            reader = csv.DictReader(file, delimiter=",", quotechar="|")
            for row in reader:
                max_km = max(max_km, int(row["km"]))
                max_price = max(max_price, int(row["price"]))
            file.seek(0)
            next(reader)
            for row in reader:
                km = float(float(row["km"]) / max_km)
                price = float(float(row["price"]) / max_price)
                data.append((km, price))
    except (FileNotFoundError, csv.Error, KeyError, ValueError):
        print("Error coming from CSV file.")
        exit(1)
    return max_km, max_price, data


def import_data_from_json(path):
    try:
        with open(path) as file:
            json_data = json.load(file)
        data = Data()
        data.theta0 = json_data["theta0"]
        data.theta1 = json_data["theta1"]
        data.max_km = json_data["max_km"]
        data.max_price = json_data["max_price"]

    except (FileExistsError, FileNotFoundError, json.JSONDecodeError, KeyError, ValueError):
        print("Error coming from JSON file.")
        exit(1)
    return data


def save_formula_values_to_json(data, path):
    try:
        with open(path, "w") as file:
            json.dump(
                {
                    "theta0": data.theta0,
                    "theta1": data.theta1,
                    "max_km": data.max_km,
                    "max_price": data.max_price,
                },
                file,
                indent=4,
            )
    except (FileExistsError, FileNotFoundError, json.JSONDecodeError, KeyError, ValueError):
        print("Error saving values to JSON file.")
        exit(1)


def show_mse_progression(mse_evolution):
    plt.clf()
    plt.plot(mse_evolution)
    plt.xlabel("Iterations")
    plt.ylabel("Mean Squared Error")
    plt.title("MSE over Trainning")
    plt.grid(True)
    plt.savefig("./mse_evolution.png")


def training_variables_model(data, data_csv, learning_rate, iterations):
    m = len(data_csv)
    alpha = learning_rate
    mse_evolution = []

    for _ in range(iterations + 1):
        sum_theta0_errors = 0
        sum_theta1_errors = 0
        mse_sum = 0

        for i in range(m):
            x = data_csv[i][0]
            y_true = data_csv[i][1]
            y_pred = data.theta0 + data.theta1 * x
            error = y_pred - y_true

            sum_theta0_errors += error
            sum_theta1_errors += error * x
            mse_sum += error**2

        temp_theta0 = data.theta0 - alpha * (1 / m) * sum_theta0_errors
        temp_theta1 = data.theta1 - alpha * (1 / m) * sum_theta1_errors

        data.theta0 = temp_theta0
        data.theta1 = temp_theta1

        mse = mse_sum / m
        mse_evolution.append(mse)
        print(f"Iteration: {_}/{iterations} - MSE = {mse}")

    show_mse_progression(mse_evolution)
    print(f"\nFinal result after {iterations} iterations")
    print("θ0:", data.theta0)
    print("θ1:", data.theta1)


def put_data_into_graph(data, data_csv):
    x = []
    y = []
    y_pred = []
    for row in data_csv:
        x.append(row[0] * data.max_km)
        y.append(row[1] * data.max_price)

    for point in x:
        x_reduced = point / data.max_km
        value = data.theta0 + data.theta1 * x_reduced
        value *= data.max_price
        y_pred.append(value)

    plt.clf()
    plt.scatter(x, y, color="blue")
    plt.plot(x, y_pred, color="red")
    plt.xlabel("Mileage (km)")
    plt.ylabel("Price")
    plt.title("Linea Regression: Price vs Mileage")
    plt.grid(True)
    plt.savefig("./regression_line.png")


def main():
    path = "./values.json"
    data = import_data_from_json(path)
    max_km, max_price, data_csv = getting_max_values_from_data_csv("./data.csv")
    if not data_csv:
        print("No data found in CSV file.")
        exit(1)
    data.update_max_values(max_km, max_price)
    learning_rate = 0.1
    iterations = 10000
    training_variables_model(data, data_csv, learning_rate, iterations)
    put_data_into_graph(data, data_csv)
    save_formula_values_to_json(data, path)
    plt.close("all")


if __name__ == "__main__":
    main()
