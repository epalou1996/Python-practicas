# This little program will be a terminal based money converter

#First we stablish the trade values in a dictionary, they will be usd based(as everything is)

dic = {"COP": 3644,
"EURO": 0.84,
"BTC" : 0.000052 ,
"MXN": 20.02 ,
"GBP": 0.75
}


# The 3 inputs we need for the process
current=input("Ingrese su moneda, COP USD EURO BTC MXN GBP en mayusculas: ")
new = input("Ingrese a la moneda que desea convertir, COP USD EURO BTC MXN GBP en mayusculas: ")
quantity = float(input("Ingrese la cantidad: "))

# As the base coin is usd, if the input coin is usd, we only need to multiply te input value for its exchange rate, if anything else, we need to also 
# divide it by the exchange rate between the input coin and usd.

if current == "USD":
	cantidad= float(dic[new])* quantity

	print("la cantidad es: " + str(cantidad))
else :
	cantidad =  (float(dic[new]) *quantity) /float(dic[current])
	print("la cantidad es: " + str(cantidad))

