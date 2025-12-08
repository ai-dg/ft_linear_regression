from data import Data


class Metrics():
    """
        Class to mesure the precision of the model (Metrics).
    """
    def __init__(self, data: Data, data_csv: list[tuple[float, float]],
                 sums_for_metrics: dict):
        self.data = data
        self.data_csv = data_csv
        self.sums_for_metrics = sums_for_metrics
        self.mse = 0
        self.mae = 0
        self.rmse = 0
        self.r_squared = 0
        self.mape = 0
        self.m = len(data_csv)

    def __str__(self):
        """
            Logic:
            - Print str of errors variables

            Return:
            - str variable
        """
        return (f"MSE: {self.mse}\nMAE: {self.mae}\nRMSE: {self.rmse}\n"
                f"R²: {self.r_squared}\nMAPE: {self.mape}\nSamples: "
                f"{self.m}")

    def ft_calculate_metrics(self):
        """
            Logic:
            - Once metrics sums is recovered from model.py,
            calculation of errors MAE, MSE, RMSE, MAPE, R2.

            Return:
            - None
        """
        if self.data.max_km == 0 or self.data.max_price == 0:
            print("Error: max_km or max_price is zero. Cannot calculate "
                  "precision.")
            return None

        self.mae = self.sums_for_metrics["mae_sum"] / self.m
        self.mse = (self.sums_for_metrics["mse_denormalized_sum"] / self.m)
        self.rmse = self.mse ** 0.5
        self.mape = (self.sums_for_metrics["mape_sum"] / self.m) * 100

        if self.sums_for_metrics["ss_tot"] != 0:
            self.r_squared = 1 - (self.sums_for_metrics["ss_res"] /
                                  self.sums_for_metrics["ss_tot"])
        else:
            self.r_squared = 0

    def ft_display_precision_metrics(self):
        """
            Logic:
            - Print all errors values and R2 interpretation

            Return:
            - None
        """
        print("\n" + "*" * 50)
        print("PRECISION METRICS")
        print("*" * 50)
        print(f"Data size: {self.m} samples")
        print()
        print("Error Metrics:")
        print(f"  MSE  (Mean Squared Error):     {self.mse:.2f}")
        print(f"  RMSE (Root Mean Squared Error): {self.rmse:.2f}")
        print(f"  MAE  (Mean Absolute Error):     {self.mae:.2f}")
        print(f"  MAPE (Mean Absolute % Error):  {self.mape:.2f}%")
        print()
        print("Performance Metrics:")
        print(f"  R² (Coefficient of Determination): "
              f"{self.r_squared:.4f}")
        print()

        if self.r_squared > 0.9:
            r2_quality = "Excellent"
        elif self.r_squared > 0.7:
            r2_quality = "Good"
        elif self.r_squared > 0.5:
            r2_quality = "Fair"
        else:
            r2_quality = "Poor"

        print("*" * 50)
        print("Interpretation:")
        print("  - Lower MSE/RMSE/MAE/MAPE = Better model")
        print("  - R² closer to 1.0 = Better fit")
        print(f"  - Current R²: {self.r_squared:.4f} ({r2_quality})")
        print("*" * 50)
