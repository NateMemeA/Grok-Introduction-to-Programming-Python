rain = input("Is it currently raining? ")
if rain == "Yes":
  print("You should take the bus.")
else:
  dist = int(input("How far in km do you need to travel? "))
  if dist > 10:
    print("You should take the bus.")
  elif dist >= 2:
    print("You should ride your bike.")
  else:
    print("You should walk.")
