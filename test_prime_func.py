import unittest
from prime import gen_prime

class TestGenPrime(unittest.TestCase):
	#tests that our func adds correctly
	#gen_prime(5) = 15

	def test_gen_prime(self):
		self.assertEqual(gen_prime(10),[2,3,5,7])

	def test_negative(self):
		self.assertEqual(gen_prime(-10),"only positive numbers allowed")

	def test_for_large_no(self):
		self.assertEqual(gen_prime(100),[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])

	def test_for_integers(self):
		self.assertEqual(gen_prime("100"),"Invalid Input!!Only numbers allowed")

	def test_for_input_greater_than_2(self):
		self.assertEqual(gen_prime(1),"Input must be greater than 2")

	def test_result_not_none(self):
		self.assertNotEqual( gen_prime(10), None)

	def test_result_not_a_dictionary(self):
		self.assertNotEqual( gen_prime(10), {})

	def test_result_not_string(self):
		self.assertNotEqual( gen_prime(10), "")

	def test_pass(self):
		self.assertTrue(True)

	def test_fail(self):
		self.assertFalse(False)



if __name__ == '__main__':
	unittest.main()
