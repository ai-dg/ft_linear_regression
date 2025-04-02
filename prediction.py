import json


def getting_data_json(path):
    try:
        with open(path) as file:
            data = json.load(file)
    except (FileExistsError, FileNotFoundError, json.JSONDecodeError):
        print("Error coming from JSON file.")
        exit(1)
    return data


def getting_price_from_predictions(path, mileage):
    try:
        estimated_price = 0
        data = getting_data_json(path)
        theta0 = data["theta0"]
        theta1 = data["theta1"]
        max_km = data["max_km"]
        max_price = data["max_price"]
        if max_km == 0 or max_price == 0:
            print("Error: max_km or max_price is zero. Cannot scale mileage.")
            exit(1)
        mileage_scaling = mileage / max_km
        price_scaling = theta0 + theta1 * mileage_scaling
        estimated_price = price_scaling * max_price
    except (KeyError, ValueError):
        print("Error coming from JSON file.")
        exit(1)
    return estimated_price


def main():
    path = "./values.json"
    try:
        mileage = float(input("Enter your mileage: "))
    except (KeyError, ValueError, KeyboardInterrupt):
        print("Try again, not valid values")
        return
    if mileage < 0:
        print("Mileage must be a positive number.")
        return
    price = getting_price_from_predictions(path, mileage)
    print(f"Price predicted ({mileage:.1f} km): {price:.2f}")


if __name__ == "__main__":
    main()
