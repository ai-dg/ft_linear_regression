import csv
import json
from data import Data


class DataProcessing():
    """
        Class to manage the data, imports/exports and return data structure
    """

    def __init__(self, path_csv: str, path_json: str):
        """
            Logic:
            - Initialize the class with the paths of models and datasets

            Return:
            - None
        """
        self.path_csv = path_csv
        self.path_json = path_json

    def __str__(self):
        """
            Logic:
            - Print datasets and json files

            Return :
            - str of paths
        """
        return (f"Path CSV: {self.path_csv}\nPath JSON: "
                f"{self.path_json}")

    def ft_getting_max_values_from_data_csv(
            self) -> tuple[float, float, list[tuple[float, float]]]:
        """
            Logic:
            - Open data with csv file and find the max_km and max_price values
            - The data is normalized with max values

            Return:
            - max_value
            - max_price
            - data : list
        """
        data: list[tuple[float, float]] = []
        max_km: float = 0.0
        max_price: float = 0.0
        try:
            with open(self.path_csv, newline="") as file:
                reader = csv.DictReader(file, delimiter=",", quotechar="|")
                rows = list(reader)
                if not rows:
                    raise ValueError("CSV file is empty.")

                for row in rows:
                    km_value = float(row["km"])
                    price_value = float(row["price"])
                    if km_value > max_km:
                        max_km = km_value
                    if price_value > max_price:
                        max_price = price_value

                if max_km == 0 or max_price == 0:
                    raise ValueError(
                        "Max km or max price is zero, cannot normalize.")

                for row in rows:
                    km = float(row["km"]) / max_km
                    price = float(row["price"]) / max_price
                    data.append((km, price))

        except (FileNotFoundError, csv.Error, KeyError, ValueError):
            print("Error coming from CSV file.")
            exit(1)

        return max_km, max_price, data

    def ft_import_data_from_json(self) -> Data:
        """
            Logic:
            - It takes weights and biais from model.json

            Return:
            - data : Data()
        """
        try:
            with open(self.path_json) as file:
                json_data = json.load(file)
            data = Data()
            data.theta0 = json_data["theta0"]
            data.theta1 = json_data["theta1"]
            data.max_km = json_data["max_km"]
            data.max_price = json_data["max_price"]
        except (FileExistsError, FileNotFoundError, json.JSONDecodeError,
                KeyError, ValueError):
            print("Error coming from JSON file.")
            exit(1)
        return data

    def ft_save_formula_values_to_json(self, data: Data):
        """
            Logic:
            - It saves the model values to the json values

            Return:
            - None
        """
        try:
            with open(self.path_json, "w") as file:
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
        except (FileExistsError, FileNotFoundError, json.JSONDecodeError,
                KeyError, ValueError):
            print("Error saving values to JSON file.")
            exit(1)

    path_csv: str
    path_json: str
