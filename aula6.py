conjunto = {1,2,3,4,5}
conjunto2 = {5,6,7,8}
conjunto_uniao = conjunto.union(conjunto2)
print('União: {}'.format(conjunto_uniao))
conjunto_interseçao = conjunto.intersection(conjunto2)
print('Interserção: {}' .format(conjunto_interseçao))
conjunto_diferença = conjunto.difference(conjunto2)
print('Diferença: {}' .format(conjunto_diferença))
conjunto_diferença2 = conjunto2.difference(conjunto)
print('Diferença2: {}' .format(conjunto_diferença2))

conjunto_a = {1,2,3}
conjunto_b = {1,2,3,4,5,6}
conjunto_subset = conjunto.issubset(conjunto_b)
print('Conjunto a é um subset de b ? {}' .format(conjunto_subset))
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print('Conjunto_b é um superset de conjunto_a ? {}' .format(conjunto_superset))

lista = ['dog', 'cat', 'leon']
conjunto_animais = set(lista)
print(conjunto_animais)

# conjunto = {1,2,3,4,5,6}
# conjunto.add(7)
# conjunto.discard(6)
# print(conjunto)