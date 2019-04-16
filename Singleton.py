
class Singleton:
	def __init__(self, cls):
		self._cls = cls
		self._instance = None
	def __call__(cls, *args, **kwargs):
		if not hasattr(cls, '_instance'):
			_instance = super().__new__(cls, *args, **kwargs)
			cls._instance = _instance
		return cls._instance

@Singleton
class MyClass(object):
	def __init__(self, name):
		self.name = name

c1 = MyClass("a")
c2 = MyClass("b")
