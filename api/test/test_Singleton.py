import unittest

from shared.Singleton import SingletonMeta

class MyClass(metaclass=SingletonMeta):
  def some_method(self):
    pass

class TestMyClass(unittest.TestCase):

  def test_is_singleton(self):
    instance1 = MyClass()
    instance2 = MyClass()
    self.assertIs(instance1, instance2)  

