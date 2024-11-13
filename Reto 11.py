from geoanalitic import distancia, pendiente
x1= float (input("Coordenada x1: \n"))
y1= float (input("Coordenada y1: \n"))
x2= float (input("Coordenada x2: \n"))
y2= float (input("Coordenada y2: \n"))

print ("El total de la distancia es: " + str(distancia(x1,y1,x2,y2)))
if (x2-x1) != 0:
    print(" El total de la pendiente es: " + str(pendiente(x1,y1,x2,y2)))
else:
    print(" El total de la pendiente es: " + str(pendiente(x1,y1,x2,y2)))

