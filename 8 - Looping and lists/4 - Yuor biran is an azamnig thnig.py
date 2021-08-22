words = input("Enter words: ")
words = words.split()
w1 = words[0]
w2 = words[1]
w1a = list(w1)
w2a = list(w2)
w1a.sort()
w2a.sort()
if w1a == w2a and w1[0] == w2[0] and w1[-1] == w2[-1]:
  print("Super Anagram!")
else:
  print("Huh?")
