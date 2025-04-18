class favanimal:

	#initialize the class
	def __init__(self,name="leopard seal", name, armlen, leglen, eyenum, tail = True, furry = False):
		self.name = name
		self.armlen = armlen
		self.leglen = leglen
		self.eyenum = eyenum
		self.tail = tail
		self.furry = furry

	def printanim(self):
		if tail == True:
			hasTail = "a"
		else:
			hasTail = "no"
		if furry == True:
			hasFur = "has"
		else:
			hasFur = "has no"
		print(f"The animal is {name}. It has {armlen} centimeters arms and {leglen} centimeters legs. It has {eyenum} number of eyes, {hasTail} tail, and {hasFur} fur")


