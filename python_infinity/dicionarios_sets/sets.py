# um set não permite elementos duplicados; também não mantém a ordem dos elementos inseridos. são os não indexados
numbers = {1, 1, 2, 3, 4, 4, 5}
uniques = set(numbers)
print(uniques)


#set comprehension (compreensão de conjunto)
set1 = {letra for letra in 'raiana' if letra not in 'aeiou'}
print(set1)


#operadores matemáticos de conjuntos
#união; utiliza-se o pipe |
planetas1 = {'Terra', 'Vênus', 'Mercúrio', 'Marte', 'Netuno'}
planetas2 = {'Terra', 'Vênus', 'Mercúrio', 'Marte', 'Saturno', 'Urano', 'Júpiter'}
print(f"união: {planetas1 | planetas2}")

#intersecção; utiliza-se o &
paises1 = {'Brasil', 'França', 'Camarões', 'México', 'Holanda'}
paises2 = {'Brasil', 'França', 'Camarões', 'Argentina', 'Inglaterra'}
print(f"intersecção: {paises1 & paises2}")

#diferença; utiliza-se o -
idiomas1 = {'Português', 'Mandarim', 'Espanhol', 'Italiano', 'Japonês'}
idiomas2 = {'Português', 'Mandarim', 'Espanhol', 'Inglês', 'Alemão', 'Francês'}
print(f"diferença: {idiomas1 - idiomas2}")

#diferença simétrica; utiliza-se o ^ {combina os elementos exclusivos de cada conjunto, excluindo os que são comuns a ambos}
cores1 = {'Amarelo', 'Vermelho', 'Azul', 'Verde', 'Roxo', 'Branco'}
cores2 = {'Amarelo', 'Vermelho', 'Azul', 'Rosa', 'Marrom', 'Preto'}
print(f"diferença simétrica: {cores1 ^ cores2}")

#conjuntos disjuntos (se não têm elementos em comum) .isdisjoint()
empregos1 = {'Programador', 'Comerciante', 'Fotógrafo', 'Professor'}
empregos2 = {'Programador', 'Comerciante', 'Engenheiro', 'Médico'}
empregos3 = {'Engenheiro', 'Médico'}
print(f"conjuntos disjuntos: {empregos2.isdisjoint(empregos3)}")


#fazer cópia de conjunto
cursos1 = {'História', 'Sistemas de Informação', 'Fisioterapia', 'Psicologia', 'Engenheiria Civil'}
cursos_copia = cursos1.copy()
print(f"Cursos de Graduação: {cursos1}")
print(f"Cursos de Graduação: {cursos_copia}")


#adicionar elementos
formas_geometricas = {'Cículo', 'Quadrado', 'Losango', 'Retângulo'}
formas_geometricas.add('Triângulo')
print(formas_geometricas)

#remover elementos .remove()
personagens = {'Goku', 'Naruto', 'Harry Potter', 'Barbie', 'Hello Kitty', 'Mia'}
personagens.remove('Naruto')
print(f"Remover elementos com .remove(): {personagens}")

#remover elementos .discard()
series = {'Friends', 'Breaking Bad', 'Modern Family'}
series.discard('Modern Family')
print(f"Remover elementos com .discard(): {series}")

#remover elementos .pop()
generos_musicais = {'Rock', 'MPB', 'Funk', 'Indie'}
generos_musicais.pop()
print(f"Remover elementos com .pop(): {generos_musicais}")

#remover todos os elementos . clear()
materias_escola = {'Matemática', 'Química', 'Física', 'Biologia'}
materias_escola.clear()
print(f"Remover TODOS os elementos com .clear(): {materias_escola}")