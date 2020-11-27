import unittest
import rect
class TestRect(unittest.TestCase):
	def test_prueba(self):
		self.assertEqual(2+2, 4)
		#comprobación test

	def test_area(self):
		area = rect.area(2,4)
		self.assertEqual(area, 8)

	def test_perim(self):
		perim = rect.perim(2,4)
		self.assertEqual(perim, 12)

	def test_centro(self):
		#devuelve un punto (x,y)
		#xmin & ymin = 0
		pcentro = rect.centro(2,4)
		self.assertEqual(pcentro, (1,2))
	def test_diag(self):
		#devuelve un vector diagonal
		#la referencia siempre es O(0,0)
		vdiag = rect.diag(2,4)
		self.assertEqual(vdiag, (2,4))
	def test_superponer(self):
		#colocamos R1 primero en el origen y comprobamos si R2 superpone
		#posibilidades: no, horizontal, vertical, completa
		sc = rect.superponer(2,2,4,4)
		sv = rect.superponer(5,1,2,4)
		sh = rect.superponer(2,4,5,1)
		sn = rect.superponer(4,4,2,2)
		self.assertEqual(sc, "completa")
		self.assertEqual(sv, "vertical")
		self.assertEqual(sh, "horizontal")
		self.assertEqual(sn, "no superpone")
	def test_inputs(self):
		#test para comprobar que los inputs son válidos (positivos no nulos)
		in1 = rect.noneg(-2,2)
		in2 = rect.noneg(2,-2)
		in3 = rect.noneg(2,2)
		self.assertEqual(in1, "no valido")
		self.assertEqual(in2, "no valido")
		self.assertEqual(in3, "valido")

		#WIP, no funciona el último