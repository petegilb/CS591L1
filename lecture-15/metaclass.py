def __setattr__(self, key, value):
  print(key, value)
  super(ConcreteClass, self).__setattr__(key, value)

def __getattr__(self, key):
  print(key)
  super(ConcreteClass, self).__getattr__(key)


class MetaClass(type):
  def __new__(cls, clsname, bases, attrs):
    print(cls, clsname, bases, attrs)
    if clsname != 'Base':
      attrs['__getattr__'] = __getattr__
      attrs['__setattr__'] = __setattr__
    return super().__new__(cls, clsname, bases, attrs)

MetaClassInstance = MetaClass('Base', (object,), {})

class ConcreteClass(MetaClassInstance):
  def __init__(self):
    self.kinan = 1
    self.rawane = 2

  def test(self):
    print('test')
'''
class ConcreteClass2(ConcreteClass):
  def test2(self):
    pass
'''

ConcreteClass()
#result = ConcreteClass()
#print(result)

#getattr(result, 'kinan')
