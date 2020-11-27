#aquí tests de abstr.py
import unittest
import abstr

class TestAbstr(unittest.TestCase):
	def test_prueba(self):
		self.assertEqual(2+2, 4)
		#dummy
	def test_palindromo(self):
		peticion = abstr.evaluar("P:palabra")
		self.assertEqual(peticion, "p")
		#si empieza por P pide función palíndromo
	def test_capicua(self):
		peticion = abstr.evaluar("C:numero")
		self.assertEqual(peticion, "c")
		#triangulamos pero con capicuas
	def test_error(self):
		peticion = abstr.evaluar("X:ERROR")
		self.assertEqual(peticion,"ERROR")
	def test_pal_espuro(self):
		p_1 = abstr.palindromo("P:ala")
		p_2 = abstr.palindromo("P:avion")
		self.assertEqual(p_1,"SI")
		self.assertEqual(p_2,"NO")
	def test_pal_parcial(self):
		p_3 = abstr.palindromo("P:ala ala ala")
		self.assertEqual(p_3,"PARCIAL")
	def test_num_capicua(self):
		c_1 = abstr.capicua("C:4231")
		self.assertEqual(c_1,"NO")
	def test_num_nonatural(self):
		c_2 = abstr.capicua("C:no soy un numero")
		self.assertEqual(c_2, "NONATURAL")

	def test_triang_pal(self):
		p_4 = abstr.palindromo("P:girafarig")
		p_5 = abstr.palindromo("P:aa uu aa")
		p_6 = abstr.palindromo("P:23sasd312e")
		self.assertEqual(p_4, "SI")
		self.assertEqual(p_5, "PARCIAL")
		self.assertEqual(p_6, "NO")
	def test_triang_num(self):
		c_3 = abstr.capicua("C:ala")
		c_4 = abstr.capicua("C:123a321")
		c_5 = abstr.capicua("C:12344321")
		c_6 = abstr.capicua("C:123")
		self.assertEqual(c_3, "NONATURAL")
		self.assertEqual(c_4, "NONATURAL")
		self.assertEqual(c_5, "SI")
		self.assertEqual(c_6, "NO")
	def test_error_final(self):
		error1 = abstr.palindromo("no salta error")
		error2 = abstr.capicua("aquí tampoco")
		self.assertEqual(error1,"ERROR")
		self.assertEqual(error2,"ERROR")


