import json
import csv
import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt


def save_theta_values(theta0, theta1, max_km, max_price):
    with open("values.json", "w") as file:
        json.dump(
            {
                "theta0": theta0,
                "theta1": theta1,
                "max_km": max_km,
                "max_price": max_price,
            },
            file,
        )


def data_import(filename):
    data = []
    max_km = 0
    max_price = 0
    try:
        with open(filename) as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            next(reader)
            for row in reader:
                max_km = max(max_km, int(row[0]))
                max_price = max(max_price, float(row[1]))
            csvfile.seek(0)
            next(reader)
            for row in reader:
                km = int(row[0]) / max_km
                price = float(row[1]) / max_price
                data.append((km, price))
    except (FileNotFoundError, csv.Error):
        print("Erreur : Problème avec le fichier CSV.")
        exit(1)
    return data, max_km, max_price


def train_model(data, learning_rate, iterations):
    m = len(data)
    theta0 = 0
    theta1 = 0
    for i in range(iterations):
        sum_errors_theta0 = 0
        sum_errors_theta1 = 0
        for km, price in data:
            pred = theta0 + theta1 * km
            error = pred - price
            sum_errors_theta0 += error
            sum_errors_theta1 += error * km
        theta0 -= learning_rate * (1 / m) * sum_errors_theta0
        theta1 -= learning_rate * (1 / m) * sum_errors_theta1
        if i % 1000 == 0:
            print(f"Iteration {i}: theta0 = {theta0}, theta1 = {theta1}")
    return theta0, theta1


def export_predictions(data, theta0, theta1, max_km, max_price):
    with open("data_model.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["km", "real price", "predicted price", "absolute error"])
        for km, price in data:
            km_actual = km * max_km
            pred_price_norm = theta0 + theta1 * km
            pred_price = pred_price_norm * max_price
            error = abs(pred_price - (price * max_price))
            writer.writerow(
                [km_actual, price * max_price, round(pred_price, 2), round(error, 2)]
            )
    print("Export des prédictions terminé dans 'data_model.csv'.")


def calculate_mae(data, theta0, theta1, max_km, max_price):
    total_error = 0
    for km, price in data:
        pred_price = (theta0 + theta1 * km) * max_price
        real_price = price * max_price
        total_error += abs(pred_price - real_price)
    mae = total_error / len(data)
    return mae


def plot_data_and_regression(data, theta0, theta1, max_km, max_price):
    x_real = [km * max_km for km, _ in data]
    y_real = [price * max_price for _, price in data]
    x_line = list(range(0, int(max_km), 1000))
    y_line = [(theta0 + theta1 * (x / max_km)) * max_price for x in x_line]
    plt.scatter(x_real, y_real, color="blue", label="Real data")
    plt.plot(x_line, y_line, color="red", label="Linear regession")
    plt.xlabel("Kilometers (km)")
    plt.ylabel("Price (€)")
    plt.title("Linear regression : Km vs price")
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    data, max_km, max_price = data_import("./data.csv")
    learning_rate = 0.1
    iterations = 10000
    theta0, theta1 = train_model(data, learning_rate, iterations)
    save_theta_values(theta0, theta1, max_km, max_price)
    print("Entraînement terminé. Paramètres sauvegardés.")
    export_predictions(data, theta0, theta1, max_km, max_price)
    mae = calculate_mae(data, theta0, theta1, max_km, max_price)
    print(f"MAE (Erreur absolue moyenne) : {mae:.2f} €")
    plot_data_and_regression(data, theta0, theta1, max_km, max_price)


if __name__ == "__main__":
    main()
