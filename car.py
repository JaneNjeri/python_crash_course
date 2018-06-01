class Car():
	"""Simple attempt to represent a car."""

	def __init__(self, make, model, year):
		"""Initialize attributes to describe a car. """
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def update_odometer(self, mileage):
		"""
		Set the odometer reading to the given value. 
		Reject the change if it attempts to roll the odometer back.
		"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back the odometer!")

	def increment_odometer(self, miles):
		"""Add given amount to the odometer reading."""
		if miles < 0:
			print("You cannot add negative miles!")
		else:
			self.odometer_reading += miles
			print("You have updated your odometer to: " + str(self.odometer_reading) + ".")
		

	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def read_odometer(self):
		"""Print a statment showing the car's milage."""
		print("This car has " + str(self.odometer_reading) + " miles on it.")

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name() )
my_new_car.read_odometer()

print("(---Below is set by instance---)")
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
print("(---Below is set by method---)")
my_new_car.update_odometer(10)
my_new_car.read_odometer()
print("(---Below this is incremented by method---)")
my_new_car.increment_odometer(1000)
my_new_car.read_odometer()

