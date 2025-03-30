import json


def load_values_from_json(filename):
    with open(filename) as file:
        return json.load(file)


def prediction(mileage):
    params = load_values_from_json("values.json")
    theta0 = params["theta0"]
    theta1 = params["theta1"]
    max_km = params["max_km"]
    max_price = params["max_price"]
    mileage_norm = mileage / max_km
    price_norm = theta0 + theta1 * mileage_norm
    price = price_norm * max_price
    return price


def main():
    try:
        mileage = float(input("Entrez le kilométrage : "))
    except ValueError:
        print("Erreur : Entrée invalide.")
        return

    price = prediction(mileage)
    print(f"Prix estimé pour {mileage:.1f} km : {price:.2f}")


if __name__ == "__main__":
    main()
