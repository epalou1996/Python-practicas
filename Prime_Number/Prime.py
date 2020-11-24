import math	#Necesario para usar raiz cuadrada con la libreria math de python

def primo(n):
	txt= 'Fue este chingon: {:.0f}'	#Pruebas con formatos para str
	if n < 2:
		return False
	elif n%2 ==0:
		return False

	raiz=int(math.sqrt(n))	#Metodo para iterar menos
	for i in range (2,raiz+1):
		print(i)
		if n%i == 0:
			num=i
			print(txt.format(num))
			return False
	return true			#Ya cuando ha descartado todas las opciones, puede afirmar que ese numero es primo





def run():
	n = int(input("Introduzca el numero que desea verificar: "))
	print(primo(n))

if __name__ == '__main__':
	run()
