class House:
	def __init__(self,pW=4,pF=2):
		self.windows = pW
		self.floors = pF
	def get_info(self):
		print("This is a", self.windows, "windows and", self.floors, "floors house.")
house1 = House()
house2 = House(2,1)
house3 = House(6,3)

print("House1")
house1.get_info()
print("-------")
print("House2")
house2.get_info()
print("-------")
print("House3")
house3.get_info()