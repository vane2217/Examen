notas_estudiantes = {
    'Juan': [3.2, 4.5, 5],
    'Maria': [4.2, 3.5, 4.3],
    'Pedro': [3.9, 2.5, 4.8]
}
for nombre, listasNotas in notas_estudiantes.items():
    suma = 0
    for nota in listasNotas:
        suma = suma + nota
        print(nombre,suma/len(listasNotas))