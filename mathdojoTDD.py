import unittest

class MathDojo:
    def __init__(self):
    	self.result = 0


    def add(self, num, *nums):
      self.result +=num
      for i in nums:
        self.result +=i
      return self


    def subtract(self, num, *nums):
      self.result -=num
      for i in nums:
        self.result -=i
      return self

md = MathDojo()

class MathDojoTests(unittest.TestCase):
    def testTwo(self):
      self.assertEqual(md.add(1).result,1)

    def testThree(self):
      self.assertEqual(md.add(1, 2).result,3)

    def testFour(self):
      self.assertEqual(md.add(1, 2, 3).result,6)

    def testFive(self):
      self.assertEqual(md.subtract(1).result, -1)

    def testSix(self):
      self.assertEqual(md.subtract(1, 2).result, -3)

    def testSeven(self):
      self.assertEqual(md.subtract(1, 2, 3).result, -6)

    def testEight(self):
      self.assertEqual(md.add(2).add(2,5,1).subtract(3,2).result, 5)

    def setUp(self):
      print("running setUp")

      md.result = 0

    def tearDown(self):
      print("running tearDown tasks")



if __name__ == '__main__':
    unittest.main() # this runs our tests

