frutas = set()

frutas.add('maçã')
frutas.add('banana')
frutas.add('uva')
frutas.add('laranja')
frutas.add('morango')

for item in frutas:
    print(item)

# if 'banana' in frutas:
#     print('Banana está presente')
# else:
#     print('Banana está ausente')

# print(f"Banana está {'presente' if 'banana' in frutas else 'ausente'}")
#################################################################################

frutas_vermelhas = set()

frutas_vermelhas.add('morango')
frutas_vermelhas.add('cereja')
frutas_vermelhas.add('framboesa')

for fruta in frutas_vermelhas:
    print(fruta)

frutas_vermelhas.discard('cereja')
print(frutas_vermelhas)

frutas_todas = frutas.union(frutas_vermelhas)
print(frutas_todas)

frutas_inter = frutas.intersection(frutas_vermelhas)