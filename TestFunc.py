import unittest
import mathfunc

class TestFunc(unittest.TestCase):
	def test_add(self):
		self.aclass = mathfunc.addc()
		self.assertEqual(4,self.aclass.add(2,2))

	def test_minus(self):
		self.mclass = mathfunc.other()
		self.assertEqual(3,self.mclass.minus(5,2))


if __name__ == '__main__':
	unittest.main(verbosity=2)