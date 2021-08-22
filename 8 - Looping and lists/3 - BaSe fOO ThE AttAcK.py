text = input("code: ")
result = [w.lower() for w in reversed(text.split()) if w[0].isupper()]
print('says:',' '.join(result))

#This was quite simple just sounds hard, you should def impress your teacher with this in 3 lines lool
