c = "electricity"
print("What is my favourite food?")
input_ = input("Guess? ")
while input_ != c:
    print("Not even close.")
    input_ = input("Guess? ")
if input_ == c:
  print("You guessed it! Buzzzz")
