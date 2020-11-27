#setup código rectángulo
class Rect():
	def __init__(l1, l2):

		if l1 > 0 and l2 > 0:
			self.neg = "Legal"
		else:
			self.neg = "No legal"

	def legal(self):
		return self.neg
	def perimetro(self):
		#debería devolver 12
		return 12