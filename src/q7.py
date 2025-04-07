class Car:
    """
    Task 1:
    Define a class named Car with the following features:
    - Attributes: make, model, year
    - Constructor (__init__) to initialize these attributes
    - Method describe_car() to print the car information as "Year Make Model"
    """

    def __init__(self, make, model, year):
        # Initialize the car's make, model, and year
        self.make = make
        self.model = model
        self.year = year

    def describe_car(self):
        # Print the car description in the format: "Year Make Model"
        print(f"{self.year} {self.make} {self.model}")


# Task 2:
# Create an instance of Car with:
# - Make: Toyota, Model: Corolla, Year: 2020
car1 = Car("Toyota", "Corolla", 2020)

# Call the describe_car method to print the car details
car1.describe_car()  # Expected output: "2020 Toyota Corolla"
