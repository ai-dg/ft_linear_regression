class Data(object):
    """
        Generic class to store all the model values
    """
    def __init__(self, theta0=0, theta1=0, max_km=0, max_price=0):
        """
            Logic:
            - Stores initial values

            Return:
            - None
        """
        self.theta0 = theta0
        self.theta1 = theta1
        self.max_km = max_km
        self.max_price = max_price

    def ft_update_max_values(self, max_km: float, max_price: float):
        """
            Logic:
            - Updates max values

            Return:
            - None
        """
        self.max_km = max_km
        self.max_price = max_price

    def __str__(self):
        """
            Logic:
            - Print variables in the class

            Return:
            - to_return : str
        """
        to_return = (f"Theta0: {self.theta0}\nTheta1: {self.theta1}\n"
                     f"max_km: {self.max_km}\nmax_price: {self.max_price}")
        return to_return

    theta0: float
    theta1: float
    max_km: float
    max_price: float
