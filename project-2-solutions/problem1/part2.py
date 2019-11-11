def null_cast(x):
  if x is None:
    raise ValueError('null_cast called on a None')

  return x
