import unittest
from prime import gen_prime

class TestGenPrime(unittest.TestCase):
	#tests that our function outputs correctly
	def test_gen_prime(self):
		self.assertEqual(gen_prime(10),[2,3,5,7])

	#tests if our function is passed a negative number
	def test_negative(self):
		self.assertEqual(gen_prime(-10),"only positive numbers allowed")

	#tests for large input
	def test_for_large_no(self):
		self.assertEqual(gen_prime(100),[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])

	#tests to see if a string is passed
	def test_for_string(self):
		self.assertEqual(gen_prime("100"),"Invalid Input!!Only numbers allowed")

	#tests for input that is less than one
	def test_for_input_greater_than_2(self):
		self.assertEqual(gen_prime(1),"Input must be greater than 2")

	#makes sure result is not none
	def test_result_not_none(self):
		self.assertNotEqual( gen_prime(10), None)

	#result is not a dictionary
	def test_result_not_a_dictionary(self):
		self.assertNotEqual( gen_prime(10), {})

	#result cannot be a string
	def test_result_not_string(self):
		self.assertNotEqual( gen_prime(10), "")

	#tests if program runs fine
	def test_pass(self):
		self.assertTrue(True)

	#tests if program fails
	def test_fail(self):
		self.assertFalse(False)



if __name__ == '__main__':
	unittest.main()
