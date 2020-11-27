global x1
global y1
global x2
global y2
#longitudes en cm

def area(x,y):
	area = x * y
	return area

def perim(x,y):
	perim = (x+y)*2
	return perim

def centro(x,y):
	pcentro = (x/2,y/2)
	return pcentro

def diag(x,y):
	vdiag = (x,y)
	return vdiag

def superponer(x1,y1,x2,y2):
	if x2 > x1 and y2 > y1:
		resultado = "completa"
	elif x2 < x1 and y2 > y1:
		resultado = "vertical"
	elif x2 > x1 and y2 < y1:
		resultado = "horizontal"
	else:
		resultado = "no superpone"
	return resultado
def noneg(x,y):
	if x1 <=0:
		input = "no valido"
	if y1 <=0:
		input = "no valido"
	if x1 > 0 and y1 > 0:
		input = "valido"
	return input

while True:
	try:
		x1 = int(input("Introduce un x1 positivo no nulo: "))
	except ValueError:
		print("Error: x1 debe ser positivo no nulo.")
		continue
	if x1 <= 0:
		print("Error: x1 debe ser positivo no nulo.")
		continue
	else:
		print("Se ha guardado el valor de x1.")
		break
while True:
	try:
		y1 = int(input("Introduce un y1 positivo no nulo: "))
	except ValueError:
		print("Error: y1 debe ser positivo no nulo.")
		continue
	if y1 <= 0:
		print("Error: y1 debe ser positivo no nulo.")
		continue
	else:
		print("Se ha guardado el valor de y1.")
		break

print("Se ha construido el rectángulo R1.")
print("Imprimiendo datos básicos de R1:")

print("Área: " + str(area(x1,y1)) + "cm²")
print("Perímetro: " + str(perim(x1,y1)) + "cm")
print("Centro: P" + str(centro(x1,y1)))
print("Diagonal: Vector" + str(diag(x1,y1)) + "desde el origen O(0,0) \n")

print("Opciones: \n 1. Cambiar parámetros R1 \n 2. Introducir R2 y superponer")

#WIP