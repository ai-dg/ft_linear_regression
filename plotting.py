import matplotlib.pyplot as plt
import matplotlib
from data import Data

matplotlib.use("GTK3Agg")


class Plotting():
    def __init__(self, data: Data = None, data_csv: list[tuple[float, float]] = None):
        self.data = data
        self.data_csv = data_csv

    def __str__(self):
        return f"Plotting"

    def ft_show_mse_progression(self, mse_evolution: list[float]):
        plt.clf()
        plt.plot(mse_evolution)
        plt.xlabel("Iterations")
        plt.ylabel("Mean Squared Error")
        plt.title("MSE over Trainning")
        plt.grid(True)
        plt.savefig("./mse_evolution.png")

    def ft_put_data_into_graph(self):
        if self.data is None or self.data_csv is None:
            print("Error: data and data_csv must be initialized.")
            return
        
        x = []
        y = []
        for row in self.data_csv:
            x.append(row[0] * self.data.max_km)
            y.append(row[1] * self.data.max_price)

        if x:
            x_min = min(x)
            x_max = max(x)
            x_line = [x_min + (x_max - x_min) * i / 99 for i in range(100)]
            y_pred = []
            for point in x_line:
                x_reduced = point / self.data.max_km
                value = self.data.theta0 + self.data.theta1 * x_reduced
                value *= self.data.max_price
                y_pred.append(value)
        else:
            x_line = []
            y_pred = []

        plt.clf()
        plt.scatter(x, y, color="blue", label="Data points")
        plt.plot(x_line, y_pred, color="red", label="Regression line")
        plt.xlabel("Mileage (km)")
        plt.ylabel("Price")
        plt.title("Linear Regression: Price vs Mileage")
        plt.legend()
        plt.grid(True)
        plt.savefig("./regression_line.png")
