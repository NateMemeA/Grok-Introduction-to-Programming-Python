a = []
prompt = "Word: "
line = input(prompt)

while line:
    a.append(line)
    line = input(prompt)

a = list(set(a))
a.sort()
print("You know",len(a),"unique word(s)!")
