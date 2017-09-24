import re

file = "example.java"
nlineas = 0
paternSpace = r'^\s*$'  #Saltos de linea en blanco
paternOne = "^\/\/.*" #Comentario tipo //
paternTwo = "^\/\*.*"  #Comentario tipo /*
paternTree = "\W\*\/.*" #Comentario tipo */
innerline = False       #Semaforo para no contar las lineas entre /* ... */

for i, line in enumerate(open(file)):
    space = re.search(paternSpace, line)
    comentOne = re.search(paternOne, line.strip())
    comentTwo = re.search(paternTwo, line.strip())
    comentTree = re.search(paternTree, line)
    if comentTwo:
        innerline = True
    if comentTree:
        innerline = False
    if not (space or comentTree or comentOne or innerline):
        nlineas += 1
print nlineas
