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

md.result = 0
print(md.add(1).result)
md.result = 0
print(md.add(1, 2).result)
md.result = 0
print(md.add(1, 2, 3).result)
md.result = 0
print(md.subtract(1).result)
md.result = 0
print(md.subtract(1, 2).result)
md.result = 0
print(md.subtract(1, 2, 3).result)
md.result = 0
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)


