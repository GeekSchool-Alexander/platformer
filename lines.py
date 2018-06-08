import numpy as np

from VectorClass import Vec2d as vec


class Line:
	def __init__(self, point1, point2 ):
		if isinstance(point1, vec) and isinstance(point2, vec):
			self.p1 = point1
			self.p2 = point2
		else:
			raise TypeError
	
	@property
	def equation(self):
		A = self.p1.y - self.p2.y
		B = self.p2.x - self.p1.x
		C = self.p1.x * self.p2.y - self.p2.x * self.p1.y
		return (A, B, C)
	
	def intersection(self, other_line, segment):
		if isinstance(segment, bool):
			if isinstance(other_line, Line):
				eq1 = self.equation
				eq2 = other_line.equation
				A1, B1, C1 = eq1[0], eq1[1], eq1[2]
				A2, B2, C2 = eq2[0], eq2[1], eq2[2]
				if A1 * B2 - A2 * B1 == 0:
					# parallel lines
					return
				a = np.array([[A1, B1], [A2, B2]])
				b = np.array([-C1, -C2])
				i = vec(np.linalg.solve(a, b).tolist())
				if not segment:
					return i
				else:
					if (self.p1.y <= i.y <= self.p2.y) and (self.p1.x <= i.x <= self.p2.x) \
						and (other_line.p1.y <= i.y <= other_line.p2.y) and (other_line.p1.x <= i.x <= other_line.p2.x):
						return i
					else:
						# point isn't on two lines
						return
			else:
				raise TypeError
		else:
			raise TypeError
