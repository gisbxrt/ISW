#aquí empiezo la abstracción con TDD

def evaluar(peticion):
	letra1 = peticion[0]
	letra2 = peticion[1]

	if letra1 == "P" and letra2 == ":":
		input = "p"
	elif letra1 == "C" and letra2 == ":":
		input = "c"
	else:
		return "ERROR"
	return input

def palindromo(p_str):
#https://www.geeksforgeeks.org/python-program-check-string-palindrome-not/
  
  valido = evaluar(p_str)
  if valido == "ERROR":
  		return "ERROR"

  str = p_str[2:]
  sinespacios = str.replace(" ", "")
  for i in range(0, int(len(str)/2)):
  	if str[i] != str [len(str)-i-1]:
  		return "NO"
  	elif str != sinespacios:
  		return "PARCIAL"
  	return "SI"

def capicua(n_str):

	valido = evaluar(n_str)
	if valido == "ERROR":
		return "ERROR"

	str = n_str[2:]
	try:
		natural = int(str)
		for i in range(0, int(len(str)/2)):
			if str[i] != str [len(str)-i-1]:
				return "NO"
		return "SI"

	except:
		return "NONATURAL"
