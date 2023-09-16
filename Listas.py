Materias = ["Matematicas", "Español", "Ciencias", "Sociales", "Fisica", "Quimica"]

#metodo Len", para calcular cuantas palabras hay en nuestra variable
print (len(Materias))

print (dir(Materias))

#Podemos accerder a los elemntos indicados la posicion:
 
print (Materias[2])

#Slicing Muestra las posiciones en un rango

print(Materias[2:5])

#Muestra todas las posiciones pero de la 3 hacia adelante
print (Materias[3:])

print (Materias[0:5])

print(Materias[-5:-1])

print(Materias[1:5])

#Tipos de datos en la lista

edades = [17,27,30,53,53,56,72,12,34]

print (type(edades) )

#Actualizar un elemento de la lista

Materias[2]="Biologia"

print (Materias[0: ] )

#Actualizar dos elemento de la lista

Materias[1:3]= "Lenguaje","Ciencias Naturales"

print (Materias[0: ] )

#Para adicionar elementos a la lista (append)

Materias.append("Religion")

print (Materias[0: ] )

#Para adicionar dos elementos a la lista (insert)

Materias.insert(3,"ingles")
print (Materias[0: ] )

#Quitar elementos de la lista (pop)

Materias.pop(3)#<- es la posicion de la lista
print (Materias[0: ])    

#Quitar elementos especificos de la lista (remove)
Materias.remove("Matematicas")
print (Materias[0: ])

#Quitar elementos de la lista (clear)

# Materias.clear()
# print (Materias[0: ])

# del Materias
# print (Materias[0: ])

#Iterar las listas con ciclo for


                    
print ("-----------------------------------|")                   
 
for i in Materias:
    print (i)

print ("-----------------------------------|")

for i in range(len(Materias)):
    print (Materias[i])
    
print ("-----------------------------------|")

for i, Materia in enumerate(Materias):
    print (i, Materia)
    
print ("-----------------------------------|")

#Usando un ciclo while

i=0
while i < len(Materias):
    print (Materias[i])
    i+=1
    print ("--------------------------------")
    
    
#lista comprehesion

[print(i) for i in Materias]

#Crear lista numero

numeros = [numero for numero in range(1,31)]

print (numeros)

    