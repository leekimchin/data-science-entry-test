class Car:
    """
    Task 1
    - Define a class named Car with attributes: make, model, year
    - Initialize these attributes in the __init__ method
    - Add a method named describe_car() that prints information about the car as "Year Make Model"
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
car1.describe_car()
