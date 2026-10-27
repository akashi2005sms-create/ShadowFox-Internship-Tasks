pi = 3.14
radius = 84 #in meters
water_per_smeter = 1.4 #in liters

area = pi*(radius**2)
total_water = area * water_per_smeter

print(f"The total area of the pond is: {area} square meters")
print(f"The total amount of water in the pond: {int(total_water)} liters")