__author__ = "Joe Wanat"

from abc import ABCMeta, abstractmethod
class Vehicle(object):
    """A vehicle for sale by Jeffco Car Dealership.


    Attributes:
        wheels: An integer representing the number of wheels the vehicle has.
        miles: The integral number of miles driven on the vehicle.
        make: The make of the vehicle as a string.
        model: The model of the vehicle as a string.
        year: The integral year the vehicle was built.
        sold_on: The date the vehicle was sold.
    """

    __metaclass__ = ABCMeta

    base_sale_price = 0
    wheels = 0
    cost_of_repair = []
    date_of_repair = []
    number_of_repairs = 0

    def __init__(self, miles, make, model, year, sold_on):
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on

    def sale_price(self):
        """Return the sale price for this vehicle as a float amount."""
        if self.sold_on is not None:
            return 0.0  # Already sold
        return 5000.0 * self.wheels

    def purchase_price(self):
        """Return the price for which we would pay to purchase the vehicle."""
        if self.sold_on is None:
            return 0.0  # Not yet sold
        return self.base_sale_price - (.10 * self.miles)

    def repair_cost(self, cost, date):
        """ set up local variables cost_of_repair, date_of_repair
        make these variables of type list so that each time
        a repair occurs, the fact can be retained."""
        self.cost_of_repair.append(cost)
        self.date_of_repair.append(date)
        self.number_of_repairs += 1

    @abstractmethod
    def vehicle_type(self):
        """"Return a string representing the type of vehicle this is."""
        pass

class Car(Vehicle):
    """A car for sale by Jeffco Car Dealership."""

    base_sale_price = 8000
    wheels = 4

    def vehicle_type(self):
        """"Return a string representing the type of vehicle this is."""
        return 'Car'

    def get_base_sale_prince(self):
        return self.base_sale_price

    def get_wheel_count(self):
    	return self.wheels

class Truck(Vehicle):
    """A truck for sale by Jeffco Car Dealership."""

    base_sale_price = 10000
    wheels = 4

    def vehicle_type(self):
        """"Return a string representing the type of vehicle this is."""
        return 'Truck'

    def get_base_sale_prince(self):
        return self.base_sale_price

    def get_wheel_count(self):
    	return self.wheels

class Motorcycle(Vehicle):
    """A motorcycle for sale by Jeffco Car Dealership."""

    base_sale_price = 4000
    wheels = 2

    def vehicle_type(self):
        """"Return a string representing the type of vehicle this is."""
        return 'Motorcycle'

    def get_base_sale_prince(self):
        return self.base_sale_price

    def get_wheel_count(self):
    	return self.wheels


def main():
    #Creates a vehicle of each type
    car = Car(142377, "Acura", "TL", 2001, None)
    truck = Truck(92871, "Ford", "F-150", 2012, 2013)
    motorcycle = Motorcycle(2132, "Harley Davidson", "Sportster 889", 2014, None)

    print "Information on " + car.vehicle_type()
    print "----------"
    print "%s %s %s with %s miles." % (car.year, car.make, car.model, car.miles)
    print "Sale Price: " + str(car.get_base_sale_prince())
    print "Wheel Count: " + str(car.get_wheel_count())
    print "Purchase Price: " + str(car.purchase_price())
    print "\n"

    print "Information on " + truck.vehicle_type()
    print "----------"
    print "%s %s %s with %s miles." % (truck.year, truck.make, truck.model, truck.miles)
    print "Sale Price: " + str(truck.get_base_sale_prince())
    print "Wheel Count: " + str(truck.get_wheel_count())
    print "Purchase Price: " + str(truck.purchase_price())
    print "\n"

    print "Information on " + motorcycle.vehicle_type()
    print "----------"
    print "%s %s %s with %s miles." % (motorcycle.year, motorcycle.make, motorcycle.model, motorcycle.miles)
    print "Sale Price: " + str(motorcycle.get_base_sale_prince())
    print "Wheel Count: " + str(motorcycle.get_wheel_count())
    print "Purchase Price: " + str(motorcycle.purchase_price())


if __name__ == "__main__":
    main()

