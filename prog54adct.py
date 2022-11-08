car1 = {
  "miles": 286,
  "gallons": 9
}

car2 = {
  "miles": 412,
  "gallons" : 40
}

car3 ={
  "miles": 361,
  "gallons" : 18
}

car4 = {
  "miles": 161,
  "gallons" : 11
}

cars = {
  "1970 vw bug": car1,
  "1979 Firebird": car2,
  "1980 suburu": car3,
  "1975 Cutlass":car4
}

print("chose a car from the following",cars.keys())
mycar = input()

carsel = cars[mycar]
miles = carsel["miles"]
gllons = carsel["gallons"]
mpg = float(miles)/gllons
print("miles:",miles)
print("gallons:",gllons)
print("MPG",round(mpg,10))