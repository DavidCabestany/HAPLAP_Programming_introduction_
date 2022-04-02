text = "kaiXo"

print("Uppercase?",text.isupper())
print("Lowercase?",text.islower())
print("First uppercase?",text[0].isupper())

print("Uppercase:",text.upper())
print("Lowercase",text.lower())
print("Capitalized:",text.capitalize())

if text.islower():
  print("is lower")
else:
  print("is not lower")