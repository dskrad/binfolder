def any_lowercase1(s):
  for c in s:
    if c.islower():
      return True
    else:
      return False

def any_lowercase2(s):
  for c in s:
    if c.islower():
      return True
    else:
      return False

def any_lowercase3(s):
  for c in s:
    flag = c.islower()
  return flag

def any_lowercase4(s):
  flag = False
  for c in s:
    flag = flag or c.islower()
  return flag

def any_lowercase5(s):
  for c in s:
    if not c.islower():
      return False
    return True

def test_f(func):
  print "testing %s:" % func.__name__
  print "NONE ", func("NONE")
  print "Some ", func("Some")
  print "somE ", func("somE")
  print

test_f(any_lowercase1)
test_f(any_lowercase2)
test_f(any_lowercase3)
test_f(any_lowercase4)
test_f(any_lowercase5)
