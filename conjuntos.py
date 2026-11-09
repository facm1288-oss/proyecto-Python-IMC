# canasta={'naranja','manzana','pera','naranja','manzana', 'platano'}
# print(canasta)
# print('naranja' in canasta)
# print('kiwi' in canasta)
# vocales = ['a', 'e', 'i', 'o', 'u','a']
# print(vocales)
# print('e'in vocales)
# vocales=(set(vocales))
# print(vocales)
# vocales1 = {'a', 'e', 'i', 'o', 'u','a'}
# vocales2 = {'a','i','u'}
# print(vocales2.issubset(vocales1))
vocales1 = {'a', 'e', 'i', 'o', 'u'}    
vocales2 = {'A','E','I','O','u'}
print(vocales1-vocales2)
print(vocales1|vocales2)
print(vocales1 & vocales2)
print(vocales1^vocales2)