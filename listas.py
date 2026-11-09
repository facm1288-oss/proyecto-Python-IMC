# vocales=['a','e','i','o','u']
# vocales [1:4] = ['e','i','o']
# print(vocales,len(vocales))
# vocales.extend({'i','i'})
# print(vocales,len(vocales))
# print(vocales.index('i'))
# print(vocales.count('i'))
# print(vocales.index('i',4))
# vocales.reverse()
# print(vocales,len(vocales))
# vocales.sort()
# print(vocales,len(vocales))

# carros =('chevrolet', 'kia','mazda','renault')
# carros = sorted(carros, key=len)
# print(carros)

vocales1=['a','e','i','o','u']
vocales2=vocales1
print(vocales1,vocales2)

print(id(vocales1) , id(vocales2))

print(id(vocales1[2]) , id(vocales2[2]))

