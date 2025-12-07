import matplotlib.pyplot as plt
import matplotlib
from data import Data
from data_processing import DataProcessing
from plotting import Plotting
from metrics import Metrics

matplotlib.use("GTK3Agg")


class Model():

    def __init__(self, data: Data, data_csv: list[tuple[float, float]], 
                 learning_rate: float, iterations: int):
        self.data = data
        self.data_csv = data_csv
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.sums_for_metrics = {
            "mse_denormalized_sum": 0,
            "mae_sum": 0,
            "total_actual": 0,
            "mape_sum": 0,
            "ss_res": 0,
            "ss_tot": 0,
        }

    def ft_training_variables_model(self):
        m = len(self.data_csv)
        alpha = self.learning_rate
        mse_evolution = []

        for iteration in range(self.iterations + 1):
            sum_theta0_errors = 0
            sum_theta1_errors = 0
            mse_sum = 0

            for i in range(m):
                x = self.data_csv[i][0]
                y_true = self.data_csv[i][1]
                y_pred = self.data.theta0 + self.data.theta1 * x
                error = y_pred - y_true

                sum_theta0_errors += error
                sum_theta1_errors += error * x
                mse_sum += error**2

                if iteration == self.iterations:
                    y_true_denormalized = y_true * self.data.max_price
                    y_pred_denormalized = y_pred * self.data.max_price
                    error_denormalized = y_pred_denormalized - y_true_denormalized
                    
                    self.sums_for_metrics["mse_denormalized_sum"] += error_denormalized**2
                    self.sums_for_metrics["mae_sum"] += abs(error_denormalized)
                    self.sums_for_metrics["total_actual"] += y_true_denormalized
                    self.sums_for_metrics["ss_res"] += error_denormalized**2
      
                    if y_true_denormalized != 0:
                        self.sums_for_metrics["mape_sum"] += abs(error_denormalized) / y_true_denormalized

            if iteration == self.iterations:
                mean_actual = self.sums_for_metrics["total_actual"] / m
                for i in range(m):
                    y_true_denormalized = self.data_csv[i][1] * self.data.max_price
                    self.sums_for_metrics["ss_tot"] += (y_true_denormalized - mean_actual)**2

                

            temp_theta0 = self.data.theta0 - alpha * (1 / m) * sum_theta0_errors
            temp_theta1 = self.data.theta1 - alpha * (1 / m) * sum_theta1_errors

            self.data.theta0 = temp_theta0
            self.data.theta1 = temp_theta1

            mse = mse_sum / m
            mse_evolution.append(mse)
            print(f"Iteration: {iteration}/{self.iterations} - MSE = {mse}")

        plotting = Plotting()
        plotting.ft_show_mse_progression(mse_evolution)
        
        print(f"\nFinal result after {self.iterations} iterations")
        print("θ0:", self.data.theta0)
        print("θ1:", self.data.theta1)

        metrics = Metrics(self.data, self.data_csv, self.sums_for_metrics)
        metrics.ft_calculate_metrics()
        metrics.ft_display_precision_metrics()


    data : Data
    data_csv : list[tuple[float, float]]
    learning_rate : float
    iterations : int


def main():
    path_csv = "./datasets/data.csv"
    path_json = "./model/model.json"

    data_processor = DataProcessing(path_csv, path_json)
    max_km, max_price, data_csv = data_processor.ft_getting_max_values_from_data_csv()
    if not data_csv:
        print("No data found in CSV file.")
        exit(1)
    data = Data(theta0=0, theta1=0, max_km=max_km, max_price=max_price)
    data.ft_update_max_values(max_km, max_price)
    
    learning_rate = 0.1
    iterations = 10000
    model = Model(data, data_csv, learning_rate, iterations)
    model.ft_training_variables_model()
    
    plotting = Plotting(data, data_csv)
    plotting.ft_put_data_into_graph()
    data_processor.ft_save_formula_values_to_json(data)
    plt.close("all")


if __name__ == "__main__":
    main()
