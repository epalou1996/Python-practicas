#Un palindromo es una frase que se puede leer igual de izq a der, que de der a izq.

#We are gonna use a more pythonlike code structure in this file, with the use of functions :3

def es_palindromo(palabra):
	palabra = palabra.replace(' ', '').lower()

	if palabra[::] == palabra[::-1]:
		return True
	else:
		return False

def run():
	palabra = input("Introduzca el palindromo: ")
	if es_palindromo(palabra):
		print("Es un palindromo!")
	else:
		print("No lo es wey")

if __name__ == '__main__':
	run()

