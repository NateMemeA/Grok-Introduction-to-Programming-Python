text = input('What did she say? ')
text = text.replace('%%', 'a')
text = text.replace('###', 'o')
text = text.replace('##', 'e')
print('She meant to say: ' + text)
