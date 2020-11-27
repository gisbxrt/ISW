import unittest
import rectangulo
class TestRectangulo(unittest.TestCase):
	def test_prueba(self):
		self.assertEqual(2+2, 4)
		#comprobación test
	def test_perimetro(self):
		#lados 2 y 4, perímetro 12
		rect = rectangulo.Rect(l1=2, 2=4)
		perimetro = rect.perimetro()
		self.assertEqual(perimetro, 12)
	def test_legal(self):
		#lados -2 y -4, no existe rectangulo
		rect= rectangulo.Rect(self, l1=-2, l2=-4)
		legal = rect.legal()
		self.assertEqual(legal, "No legal")
	#def test_area(self):
	    #rect = rectangulo.Rect(2,4)
	    #area = rect.area()
	    #self.assertEqual(area, 8)
	#def test_centro(self):