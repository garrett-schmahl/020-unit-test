import unittest

def reverse_list(list):
  for i in range(int(len(list)/2)):
    list[i], list[len(list)-1-i] = list[len(list)-1-i], list[i]
  return list


def isPalindrome(word):
  reversed_string = ""
  for i in range(len(word)-1, -1, -1): #reversed loop for flavor =D
    reversed_string += word[i]
  if word == reversed_string:
    return True
  else:
    return False


def yourChangeMaam(amount): #screw loops this is faster =D
  quarter = (amount-amount%25)/25
  amount -= quarter * 25
  dime = (amount-amount%10)/10
  amount -= dime * 10
  nickel = (amount-amount%5)/5
  amount -= nickel * 5
  return [quarter,dime,nickel,amount]


def recursionBaby(value):
  if value > 1:
    value = value*recursionBaby(value-1)
  return value


def recursiveFib(value): # oh god my brain
  if value==0 or value==1:
    return value
  else:
    return recursiveFib(value-1)+recursiveFib(value-2)


# initialized by creating a class that inherits from unittest.TestCase
class IsEvenTests(unittest.TestCase):
    def testTwo(self):
      self.assertEqual(reverse_list([1,3,5]), [5,3,1])
      self.assertEqual(reverse_list([1,2,3,4]), [4,3,2,1])
      self.assertEqual(reverse_list([1,2]), [2,1])
      self.assertNotEqual(reverse_list([1,3,5,"terrycloth"]), [5,3,1])


    def testThree(self):
      self.assertTrue(isPalindrome("racecar"))
      self.assertFalse(isPalindrome("barnacle"))
      self.assertTrue(isPalindrome("kayak"))
      self.assertTrue(isPalindrome("rotator"))
      self.assertTrue(isPalindrome("step on no pets"))
      self.assertFalse(isPalindrome("document"))
      self.assertFalse(isPalindrome("trailer"))


    def testFour(self):
      self.assertEqual(yourChangeMaam(87), [3,1,0,2])
      self.assertEqual(yourChangeMaam(17), [0,1,1,2])
      self.assertEqual(yourChangeMaam(5), [0,0,1,0])
      self.assertEqual(yourChangeMaam(63), [2,1,0,3])
      self.assertEqual(yourChangeMaam(42), [1,1,1,2])     


    def testFive(self):
      self.assertEqual(recursionBaby(5), 120)
      self.assertEqual(recursionBaby(4), 24)
      self.assertEqual(recursionBaby(6), 720)


    def testSix(self):
      self.assertEqual(recursiveFib(5),5)
      self.assertEqual(recursiveFib(4),3)
      self.assertEqual(recursiveFib(3),2)
      self.assertEqual(recursiveFib(2),1)


    def setUp(self):
      print("running setUp")


    def tearDown(self):
      print("running tearDown tasks")


if __name__ == '__main__':
    unittest.main() # this runs our tests

