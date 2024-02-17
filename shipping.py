weight = 41.5
premium = 125
#Ground Shipping
if weight <= 2:
  print("Ground Price per pound is $", weight * 1.5 + 20, "or a premium fee of $", premium)
elif weight > 2 and weight <= 6:
    print("Ground Price per pound is $", weight * 3 + 20, "or a premium fee of $", premium)
elif weight > 6 and weight <= 10:
      print("Ground Price per pound is $", weight * 4 + 20, "or a premium fee of $", premium)
else: 
    print("Ground Price per pound is $", weight * 4.75 + 20, "or a premium fee of $", premium)

#Drone shipping
if weight <= 2:
  print("Drone Price per pound is $", weight * 4.5)
elif weight > 2 and weight <= 6:
    print("Drone Price per pound is $", weight * 9)
elif weight > 6 and weight <= 10:
      print("Drone Price per pound is $", weight * 12)
else: 
    print("Drone Price per pound is $", weight * 14.75)
