def single_01(cls):
	s = []
	def wrap(*args, **kwargs):
		if not s:
			s.append(cls(*args, **kwargs))
		return s
	return wrap

@single_01
class A(object):
	def __init__(self, name):
		self.name = name



