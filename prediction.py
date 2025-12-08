from data_processing import DataProcessing
from data import Data
import sys


def ft_getting_price_from_predictions(data: Data, mileage: float) -> float:
    """
        Logic:
        - Formula of linear regression y

        Return:
        - None
    """
    try:
        if data.max_km == 0 or data.max_price == 0:
            price_scaling = (data.theta0 + data.theta1 * mileage)
            estimated_price = price_scaling * data.max_price
            return estimated_price
        mileage_scaling = mileage / data.max_km
        price_scaling = (data.theta0 + data.theta1 * mileage_scaling)
        estimated_price = price_scaling * data.max_price
        return estimated_price
    except (KeyError, ValueError):
        print("Error calculating price prediction.")
        sys.exit(1)


def main():
    path_json = "./model/model.json"
    path_csv = "./datasets/data.csv"

    data_processor = DataProcessing(path_csv, path_json)
    data = data_processor.ft_import_data_from_json()

    try:
        mileage = float(input("Enter your mileage: "))
    except (KeyError, ValueError, KeyboardInterrupt):
        print("Try again, not valid values")
        return

    if mileage < 0:
        print("Mileage must be a positive number.")
        return

    price = ft_getting_price_from_predictions(data, mileage)
    print(f"Price predicted ({mileage:.1f} km): {price:.2f}")


if __name__ == "__main__":
    main()
